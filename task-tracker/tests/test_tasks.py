"""
Test suite for Task Tracker API
Part 2.4: Tests and Break Test Validation
Expanded with Module 3 Edge-Case Verifications
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.storage import _reset


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_storage():
    """
    Automatically reset the in-memory storage before every single test.
    This guarantees state isolation and prevents test leakage.
    """
    _reset()


# ============================================================
# CREATE / POST /tasks
# ============================================================

def test_create_task_valid(client):
    """POST /tasks with valid data returns 201 and creates task."""
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test task"
    assert data["status"] == "ToDo"
    assert data["priority"] == "Medium"
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_create_task_with_all_fields(client):
    """POST /tasks with all fields returns 201."""
    response = client.post(
        "/tasks", 
        json={
            "title": "Deploy app",
            "description": "Deploy to production",
            "priority": "High",
            "assignee": "Alice"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Deploy app"
    assert data["description"] == "Deploy to production"
    assert data["priority"] == "High"
    assert data["assignee"] == "Alice"


def test_create_task_empty_title_rejected(client):
    """POST /tasks with empty title returns 422."""
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 422


def test_create_task_whitespace_title_rejected(client):
    """POST /tasks with whitespace-only title returns 422."""
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 422


def test_create_task_title_over_200_chars_rejected(client):
    """POST /tasks with title > 200 chars returns 422."""
    long_title = "x" * 201
    response = client.post("/tasks", json={"title": long_title})
    assert response.status_code == 422


def test_create_task_extra_field_rejected(client):
    """POST /tasks with extra field returns 422."""
    response = client.post("/tasks", json={"title": "Test", "made_up": "field"})
    assert response.status_code == 422


# ============================================================
# LIST / GET /tasks
# ============================================================

def test_list_tasks_empty(client):
    """GET /tasks with no tasks returns 200 with empty list."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_multiple(client):
    """GET /tasks returns all tasks."""
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    client.post("/tasks", json={"title": "Task 3"})
    
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 3
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["title"] == "Task 2"
    assert tasks[2]["title"] == "Task 3"


def test_list_tasks_filter_by_priority(client):
    """GET /tasks?priority=High filters by priority."""
    client.post("/tasks", json={"title": "High task", "priority": "High"})
    client.post("/tasks", json={"title": "Low task", "priority": "Low"})
    client.post("/tasks", json={"title": "Medium task", "priority": "Medium"})
    
    response = client.get("/tasks?priority=High")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["priority"] == "High"


def test_list_tasks_filter_by_status(client):
    """GET /tasks?status=InProgress filters by status."""
    task1_id = client.post("/tasks", json={"title": "Task 1"}).json()["id"]
    client.post("/tasks", json={"title": "Task 2"})
    
    # Move task1 to InProgress
    client.patch(f"/tasks/{task1_id}", json={"status": "InProgress"})
    
    response = client.get("/tasks?status=InProgress")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["status"] == "InProgress"


# ============================================================
# GET BY ID / GET /tasks/{id}
# ============================================================

def test_get_task_by_id_found(client):
    """GET /tasks/{id} returns task if found."""
    created = client.post("/tasks", json={"title": "Test task"}).json()
    task_id = created["id"]
    
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Test task"


def test_get_task_by_id_not_found(client):
    """GET /tasks/{id} returns 404 if not found."""
    response = client.get("/tasks/999")
    assert response.status_code == 404


# ============================================================
# UPDATE / PATCH /tasks/{id}
# ============================================================

def test_update_task_title(client):
    """PATCH /tasks/{id} updates title."""
    task_id = client.post("/tasks", json={"title": "Original"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"title": "Updated"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated"


def test_update_task_multiple_fields(client):
    """PATCH /tasks/{id} updates multiple fields."""
    task_id = client.post("/tasks", json={"title": "Original"}).json()["id"]
    
    response = client.patch(
        f"/tasks/{task_id}",
        json={"title": "New title", "description": "New description", "priority": "High"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New title"
    assert data["description"] == "New description"
    assert data["priority"] == "High"


def test_update_task_not_found(client):
    """PATCH /tasks/{id} returns 404 if not found."""
    response = client.patch("/tasks/999", json={"title": "Updated"})
    assert response.status_code == 404


def test_update_task_invalid_title(client):
    """PATCH /tasks/{id} with empty title returns 422."""
    task_id = client.post("/tasks", json={"title": "Original"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"title": ""})
    assert response.status_code == 422


# ============================================================
# MODULE 3 CANDIDATE PATCH EDGE CASES
# ============================================================

def test_patch_unsupported_status_error(client):
    """PATCH /tasks/{id} with an unsupported status like 'Archived' returns 422."""
    task_id = client.post("/tasks", json={"title": "Test Task"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"status": "Archived"})
    assert response.status_code == 422


def test_patch_invalid_priority_error(client):
    """PATCH /tasks/{id} with an invalid priority like 'Urgent' returns 422."""
    task_id = client.post("/tasks", json={"title": "Test Task"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"priority": "Urgent"})
    assert response.status_code == 422


def test_patch_non_existent_id(client):
    """PATCH /tasks/{id} to a task ID that does not exist returns 404."""
    response = client.patch("/tasks/99999", json={"status": "InProgress"})
    assert response.status_code == 404


def test_patch_extra_fields_rejected(client):
    """PATCH /tasks/{id} with undefined body arguments returns 422 validation error."""
    task_id = client.post("/tasks", json={"title": "Test Task"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"made_up_attribute": "invalid"})
    assert response.status_code == 422


# ============================================================
# STATUS TRANSITIONS
# ============================================================

def test_transition_todo_to_inprogress_valid(client):
    """Status transition ToDo to InProgress is valid."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"status": "InProgress"})
    assert response.status_code == 200
    assert response.json()["status"] == "InProgress"


def test_transition_inprogress_to_done_valid(client):
    """Status transition InProgress to Done is valid."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    client.patch(f"/tasks/{task_id}", json={"status": "InProgress"})
    response = client.patch(f"/tasks/{task_id}", json={"status": "Done"})
    assert response.status_code == 200
    assert response.json()["status"] == "Done"


def test_transition_done_to_inprogress_valid(client):
    """Status transition Done to InProgress is valid."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    client.patch(f"/tasks/{task_id}", json={"status": "InProgress"})
    client.patch(f"/tasks/{task_id}", json={"status": "Done"})
    response = client.patch(f"/tasks/{task_id}", json={"status": "InProgress"})
    assert response.status_code == 200
    assert response.json()["status"] == "InProgress"


def test_transition_todo_to_done_invalid(client):
    """Status transition ToDo to Done is invalid (422)."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"status": "Done"})
    assert response.status_code == 422


def test_transition_inprogress_to_todo_invalid(client):
    """Status transition InProgress to ToDo is invalid (422)."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    client.patch(f"/tasks/{task_id}", json={"status": "InProgress"})
    response = client.patch(f"/tasks/{task_id}", json={"status": "ToDo"})
    assert response.status_code == 422


def test_transition_done_to_todo_invalid(client):
    """Status transition Done to ToDo is invalid (422)."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    client.patch(f"/tasks/{task_id}", json={"status": "InProgress"})
    client.patch(f"/tasks/{task_id}", json={"status": "Done"})
    response = client.patch(f"/tasks/{task_id}", json={"status": "ToDo"})
    assert response.status_code == 422


def test_transition_same_to_same_invalid(client):
    """Status transition same to same is invalid (422)."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    response = client.patch(f"/tasks/{task_id}", json={"status": "ToDo"})
    assert response.status_code == 422


# ============================================================
# DELETE / DELETE /tasks/{id}
# ============================================================

def test_delete_task_success(client):
    """DELETE /tasks/{id} returns 204 and deletes task."""
    task_id = client.post("/tasks", json={"title": "Task"}).json()["id"]
    
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verify task is deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404


def test_delete_task_not_found(client):
    """DELETE /tasks/{id} returns 404 if not found."""
    response = client.delete("/tasks/999")
    assert response.status_code == 404


def test_delete_task_removes_from_list(client):
    """DELETE /tasks/{id} removes task from list."""
    task1_id = client.post("/tasks", json={"title": "Task 1"}).json()["id"]
    task2_id = client.post("/tasks", json={"title": "Task 2"}).json()["id"]
    
    client.delete(f"/tasks/{task1_id}")
    
    response = client.get("/tasks")
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["id"] == task2_id


# ============================================================
# HEALTH AND ROOT ENDPOINTS
# ============================================================

def test_health_endpoint(client):
    """GET /health returns 200 with status=ok."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "timestamp" in data


def test_root_endpoint(client):
    """GET / returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Task Tracker API"

def test_create_task_with_valid_tags(client):
    """POST /tasks saves sanitized tags successfully."""
    response = client.post("/tasks", json={
        "title": "Clean Garage",
        "tags": [" home ", "weekend", "   "]  # Contains trailing space, and empty spaces
    })
    assert response.status_code == 200
    data = response.json()
    assert "tags" in data
    # Whitespace must be stripped, and empty strings must be ignored
    assert data["tags"] == ["home", "weekend"]

def test_create_task_invalid_tags_rejected(client):
    """POST /tasks rejects more than 5 tags or tags longer than 20 characters."""
    # Test length validation
    response_long = client.post("/tasks", json={
        "title": "Task A",
        "tags": ["a" * 21]
    })
    assert response_long.status_code == 422

    # Test count validation
    response_count = client.post("/tasks", json={
        "title": "Task B",
        "tags": ["1", "2", "3", "4", "5", "6"]
    })
    assert response_count.status_code == 422


def test_filter_tasks_by_text_search(client):
    """GET /tasks?search=deploy filters tasks by title and description case-insensitively."""
    client.post("/tasks", json={"title": "Deploy production app", "description": "urgent stuff"})
    client.post("/tasks", json={"title": "Write documentation", "description": "Need to deploy to docs site"})
    client.post("/tasks", json={"title": "Buy groceries"})

    # Case-insensitive title match
    r1 = client.get("/tasks?search=DEPLOY")
    assert r1.status_code == 200
    assert len(r1.json()) == 2

    # Description match
    r2 = client.get("/tasks?search=docs")
    assert r2.status_code == 200
    assert len(r2.json()) == 1

def test_filter_tasks_combined_query(client):
    """GET /tasks with multiple query parameters returns the correct filtered subset."""
    client.post("/tasks", json={"title": "Fix bug", "priority": "High", "tags": ["bug"]})
    client.post("/tasks", json={"title": "Write test cases", "priority": "Medium", "tags": ["bug"]})
    
    # Combined: tag is 'bug' and priority is 'High'
    response = client.get("/tasks?tag=bug&priority=High")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Fix bug"