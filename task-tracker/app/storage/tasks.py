# In-memory task storage with JSON file persistence
# Module 2.1: Storage layer for Task Tracker API

import json
import os
from typing import Dict, List, Optional
from datetime import datetime
from app.models.task import TaskStatus, TaskPriority

# Storage file location
STORAGE_FILE = "tasks.json"

# In-memory storage: dict mapping task id -> task dict
_tasks: Dict[int, dict] = {}
_next_id: int = 1


def _load_from_file():
    """Load tasks from JSON file on startup."""
    global _tasks, _next_id
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, 'r') as f:
                data = json.load(f)
                _tasks = {int(k): v for k, v in data.get("tasks", {}).items()}
                _next_id = data.get("next_id", 1)
        except (json.JSONDecodeError, IOError):
            _tasks = {}
            _next_id = 1
    else:
        _tasks = {}
        _next_id = 1


def _save_to_file():
    """Persist current tasks to JSON file."""
    data = {
        "tasks": _tasks,
        "next_id": _next_id,
        "last_updated": datetime.utcnow().isoformat()
    }
    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def add_task(title: str, description: Optional[str], priority: str, assignee: Optional[str]) -> dict:
    """
    Create a new task in storage.
    Returns the created task dict with id, status, created_at, updated_at.
    """
    global _next_id
    
    task_id = _next_id
    _next_id += 1
    now = datetime.utcnow().isoformat()
    
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": TaskStatus.TODO.value,
        "priority": priority,
        "assignee": assignee,
        "created_at": now,
        "updated_at": now,
    }
    
    _tasks[task_id] = task
    _save_to_file()
    return task


def get_all_tasks() -> List[dict]:
    """
    Get all tasks.
    Returns list of task dicts, empty list if no tasks.
    """
    return list(_tasks.values())


def get_task_by_id(task_id: int) -> Optional[dict]:
    """
    Get a single task by id.
    Returns task dict if found, None if not found.
    """
    return _tasks.get(task_id)


def get_tasks_by_status(status: str) -> List[dict]:
    """
    Get tasks filtered by status.
    Returns list of matching task dicts.
    """
    return [task for task in _tasks.values() if task["status"] == status]


def get_tasks_by_priority(priority: str) -> List[dict]:
    """
    Get tasks filtered by priority.
    Returns list of matching task dicts.
    """
    return [task for task in _tasks.values() if task["priority"] == priority]


def update_task(task_id: int, title: Optional[str], description: Optional[str], 
                priority: Optional[str], assignee: Optional[str]) -> Optional[dict]:
    """
    Partially update a task (not status).
    Only updates fields that are provided (not None).
    Returns updated task dict if found, None if not found.
    """
    if task_id not in _tasks:
        return None
    
    task = _tasks[task_id]
    
    if title is not None:
        task["title"] = title
    if description is not None:
        task["description"] = description
    if priority is not None:
        task["priority"] = priority
    if assignee is not None:
        task["assignee"] = assignee
    
    task["updated_at"] = datetime.utcnow().isoformat()
    _save_to_file()
    return task


def update_task_status(task_id: int, new_status: str) -> Optional[dict]:
    """
    Update task status.
    Returns updated task dict if found, None if not found.
    Note: Status transition validation happens in business_rules.py.
    """
    if task_id not in _tasks:
        return None
    
    task = _tasks[task_id]
    task["status"] = new_status
    task["updated_at"] = datetime.utcnow().isoformat()
    _save_to_file()
    return task


def delete_task(task_id: int) -> bool:
    """
    Delete a task.
    Returns True if deleted, False if not found.
    """
    if task_id in _tasks:
        del _tasks[task_id]
        _save_to_file()
        return True
    return False


def _reset():
    """
    Reset storage to empty state. Used for testing.
    """
    global _tasks, _next_id
    _tasks = {}
    _next_id = 1
    # Don't save to file; this is test-only.


# Load tasks from file on module import
_load_from_file()
