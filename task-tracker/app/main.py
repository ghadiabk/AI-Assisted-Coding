# Task Tracker FastAPI Application
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Import models
from app.models.task import TaskCreate, TaskPriority, TaskResponse, TaskStatus, TaskUpdate

# Import storage helpers
from app.storage.tasks import (
    add_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    get_tasks_by_priority,
    get_tasks_by_status,
    update_task,
    update_task_status,
)

# Import business logic
from app.business_rules import validate_status_transition

# Initialize app
app = FastAPI(
    title="Task Tracker API",
    description="A simple task management API built with FastAPI",
    version="0.1.0"
)

# ============================================================
# CORS Middleware Configuration
# ============================================================
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Health and System Endpoints
# ============================================================

@app.get("/health", response_class=JSONResponse, status_code=200)
async def health_check() -> JSONResponse:
    """Health check endpoint to verify system availability.

    Returns:
        JSONResponse: HTTP 200 response containing operational status and UTC timestamp.
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )


@app.get("/", status_code=200)
async def root() -> dict:
    """Root application endpoint providing API meta info.

    Returns:
        dict: Basic API welcome payload and documentation links.
    """
    return {
        "message": "Task Tracker API",
        "docs_url": "/docs",
        "health_url": "/health"
    }


# ============================================================
# CRUD Endpoints
# ============================================================

@app.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(task: TaskCreate) -> TaskResponse:
    """Creates a new task in storage.

    Args:
        task (TaskCreate): Validated task creation request payload containing title,
            optional description, priority, assignee, and tags.

    Returns:
        TaskResponse: Newly created task record with server-generated ID, status ("ToDo"),
            and creation/update timestamps.

    Raises:
        HTTPException: HTTP 422 Unprocessable Entity if input fields fail model validation rules.
    """
    task_dict = add_task(
        title=task.title,
        description=task.description,
        priority=task.priority.value if task.priority else TaskPriority.MEDIUM.value,
        assignee=task.assignee,
        tags=task.tags
    )
    return TaskResponse(**task_dict)


@app.get("/tasks", response_model=List[TaskResponse], status_code=200)
async def list_tasks(
    status: Optional[str] = Query(None, description="Filter by TaskStatus (ToDo, InProgress, Done)"),
    priority: Optional[str] = Query(None, description="Filter by TaskPriority (Low, Medium, High)"),
    search: Optional[str] = Query(None, description="Substring search in title or description"),
    tag: Optional[str] = Query(None, description="Exact tag string match (case-insensitive)")
) -> List[TaskResponse]:
    """Retrieves all tasks with optional sequential filtering parameters.

    Args:
        status (Optional[str]): Task status string to filter by.
        priority (Optional[str]): Task priority string to filter by.
        search (Optional[str]): Text string to search in title and description.
        tag (Optional[str]): Tag string to match in task tag arrays.

    Returns:
        List[TaskResponse]: List of task records matching all combined filter criteria.
            Returns an empty list `[]` if no records match.
    """
    tasks = get_all_tasks()

    if status:
        tasks = [t for t in tasks if t.get("status") == status]
        
    if priority:
        tasks = [t for t in tasks if t.get("priority") == priority]
        
    if tag:
        tag_lower = tag.lower()
        tasks = [
            t for t in tasks 
            if any(tag_lower == t_tag.lower() for t_tag in t.get("tags", []))
        ]
        
    if search:
        search_lower = search.lower()
        tasks = [
            t for t in tasks 
            if (t.get("title") and search_lower in t["title"].lower()) or 
               (t.get("description") and search_lower in t["description"].lower())
        ]
    
    return [TaskResponse(**task) for task in tasks]


@app.get("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(
    task_id: int = Path(..., gt=0, description="Positive integer task ID")
) -> TaskResponse:
    """Retrieves a single task record by its unique identifier.

    Args:
        task_id (int): Unique task ID (must be > 0).

    Returns:
        TaskResponse: The requested task record if found.

    Raises:
        HTTPException: HTTP 404 Not Found if no task exists with the given ID.
    """
    task_dict = get_task_by_id(task_id)
    if not task_dict:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    return TaskResponse(**task_dict)


@app.patch("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
async def update_task_endpoint(
    task_id: int = Path(..., gt=0, description="Positive integer task ID"),
    task_update: TaskUpdate = None
) -> TaskResponse:
    """Partially updates an existing task, including status transitions and detail fields.

    Args:
        task_id (int): Unique task ID (must be > 0).
        task_update (TaskUpdate): Partial task update payload with optional fields.

    Returns:
        TaskResponse: The updated task record.

    Raises:
        HTTPException: HTTP 404 Not Found if task ID does not exist.
        HTTPException: HTTP 422 Unprocessable Entity if requested status transition is invalid
            or input fields fail validation.
    """
    task_dict = get_task_by_id(task_id)
    if not task_dict:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    updated_task_dict = task_dict.copy()

    # 1. Handle status updates and transitions
    if task_update and task_update.status is not None:
        current_status = task_dict["status"]
        new_status = task_update.status.value
        
        # Validate status transition
        if not validate_status_transition(current_status, new_status):
            raise HTTPException(
                status_code=422, 
                detail=f"Invalid status transition from {current_status} to {new_status}"
            )
        updated_task_dict = update_task_status(task_id, new_status)
    
    # 2. Handle other fields (title, description, priority, assignee, tags)
    if task_update:
        has_other_updates = any(
            getattr(task_update, field) is not None 
            for field in ["title", "description", "priority", "assignee", "tags"]
        )
        
        if has_other_updates:
            updated_task_dict = update_task(
                task_id,
                title=task_update.title if task_update.title is not None else None,
                description=task_update.description if task_update.description is not None else None,
                priority=task_update.priority.value if task_update.priority is not None else None,
                assignee=task_update.assignee if task_update.assignee is not None else None,
                tags=task_update.tags if task_update.tags is not None else None
            )
    
    if not updated_task_dict:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    return TaskResponse(**updated_task_dict)


@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task_endpoint(
    task_id: int = Path(..., gt=0, description="Positive integer task ID")
) -> None:
    """Deletes a task record from storage by its ID.

    Args:
        task_id (int): Unique task ID (must be > 0).

    Returns:
        None: Returns HTTP 204 No Content upon successful deletion.

    Raises:
        HTTPException: HTTP 404 Not Found if task ID does not exist.
    """
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    return None