# Task Tracker FastAPI Application
from datetime import datetime
from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List

# Import models
from app.models import TaskCreate, TaskUpdate, TaskResponse, TaskStatus, TaskPriority

# Import storage helpers
from app.storage import (
    add_task, get_all_tasks, get_task_by_id, 
    get_tasks_by_status, get_tasks_by_priority,
    update_task, update_task_status, delete_task
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


# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    Returns HTTP 200 with status and timestamp.
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Task Tracker API",
        "docs_url": "/docs",
        "health_url": "/health"
    }


# ============================================================
# CRUD Endpoints
# ============================================================

@app.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(task: TaskCreate):
    """
    Create a new task.
    
    Request body:
    - title: str (required, 1-200 chars, no leading/trailing whitespace)
    - description: str (optional, max 2000 chars, default None)
    - priority: TaskPriority (optional, default MEDIUM)
    - assignee: str (optional, max 255 chars, default None)
    - status: TaskStatus (optional, default TODO)
    
    Response: 201 Created with full TaskResponse including id, created_at, updated_at
    """
    # Create task using storage layer
    task_dict = add_task(
        title=task.title,
        description=task.description,
        priority=task.priority.value if task.priority else TaskPriority.MEDIUM.value,
        assignee=task.assignee
    )
    
    return TaskResponse(**task_dict)


@app.get("/tasks", response_model=List[TaskResponse], status_code=200)
async def list_tasks(status: Optional[str] = Query(None), priority: Optional[str] = Query(None)):
    """
    Get all tasks with optional filtering.
    
    Query parameters (optional):
    - status: Filter by TaskStatus (ToDo, InProgress, Done)
    - priority: Filter by TaskPriority (Low, Medium, High)
    
    Response: 200 OK with list of TaskResponse objects
    """
    # Get filtered tasks
    if status and priority:
        # Filter by both status and priority
        tasks = [t for t in get_all_tasks() if t["status"] == status and t["priority"] == priority]
    elif status:
        # Filter by status only
        tasks = get_tasks_by_status(status)
    elif priority:
        # Filter by priority only
        tasks = get_tasks_by_priority(priority)
    else:
        # No filters - return all
        tasks = get_all_tasks()
    
    return [TaskResponse(**task) for task in tasks]


@app.get("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(task_id: int = Path(..., gt=0)):
    """
    Get a single task by ID.
    
    Path parameters:
    - task_id: int (positive integer)
    
    Response: 200 OK with TaskResponse if found, 404 Not Found if not found
    """
    task_dict = get_task_by_id(task_id)
    if not task_dict:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    return TaskResponse(**task_dict)


@app.patch("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
async def update_task_endpoint(task_id: int = Path(..., gt=0), task_update: TaskUpdate = None):
    """
    Partially update a task.
    
    Path parameters:
    - task_id: int (positive integer)
    
    Request body (all optional):
    - title: str (1-200 chars)
    - description: str (max 2000 chars)
    - status: TaskStatus (TODO, IN_PROGRESS, DONE) - validates transitions
    - priority: TaskPriority
    - assignee: str (max 255 chars)
    
    Response: 
    - 200 OK with updated TaskResponse if found
    - 404 Not Found if task not found
    - 422 Unprocessable Entity if status transition is invalid
    """
    # Get current task
    task_dict = get_task_by_id(task_id)
    if not task_dict:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    # Track if updates actually occurred
    updated_task_dict = task_dict.copy()

    # 1. Handle status updates and transitions
    if task_update.status is not None:
        current_status = task_dict["status"]
        new_status = task_update.status.value
        
        # Always validate status transition (including same-to-same transitions)
        if not validate_status_transition(current_status, new_status):
            raise HTTPException(
                status_code=422, 
                detail=f"Invalid status transition from {current_status} to {new_status}"
            )
        updated_task_dict = update_task_status(task_id, new_status)
    
    # 2. Handle other fields (title, description, priority, assignee)
    has_other_updates = any(
        getattr(task_update, field) is not None 
        for field in ["title", "description", "priority", "assignee"]
    )
    
    if has_other_updates:
        updated_task_dict = update_task(
            task_id,
            title=task_update.title if task_update.title is not None else None,
            description=task_update.description if task_update.description is not None else None,
            priority=task_update.priority.value if task_update.priority is not None else None,
            assignee=task_update.assignee if task_update.assignee is not None else None
        )
    
    if not updated_task_dict:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    return TaskResponse(**updated_task_dict)


@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task_endpoint(task_id: int = Path(..., gt=0)):
    """
    Delete a task.
    
    Path parameters:
    - task_id: int (positive integer)
    
    Response: 204 No Content if deleted, 404 Not Found if not found
    """
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
    return None