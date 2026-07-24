# Task Tracker Pydantic v2 Models
# Strict validation: TaskStatus and TaskPriority enums, title validation,
# server-managed fields excluded from input models.

from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List
from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    """Task status enum — allowed states for a task."""
    TODO = "ToDo"
    IN_PROGRESS = "InProgress"
    DONE = "Done"


class TaskPriority(str, Enum):
    """Task priority enum — allowed priority levels."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class TaskCreate(BaseModel):
    """
    Schema for creating a new task.
    Accepts: title (required), description (optional), priority (optional, default Medium),
    assignee (optional), status (optional, default TODO), tags (optional, default empty list).
    Rejects: id, created_at, updated_at (server-managed).
    """
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(default=" ", max_length=2000)
    status: TaskStatus = Field(default=TaskStatus.TODO)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM)
    assignee: Optional[str] = Field(default=None, max_length=255)
    tags: Optional[List[str]] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid")  # Reject unknown fields

    @field_validator("title", mode="before")
    @classmethod
    def validate_title_not_blank(cls, v: str) -> str:
        """Title must not be empty or whitespace-only after stripping."""
        if isinstance(v, str):
            stripped = v.strip()
            if not stripped:
                raise ValueError("title cannot be empty or whitespace-only")
            return stripped
        raise ValueError("title must be a string")

    @field_validator("tags", mode="before")
    @classmethod
    def validate_tags(cls, v: Optional[List[str]]) -> List[str]:
        """Tags must be a list of sanitized, non-empty, and limited strings."""
        if v is None:
            return []
        if not isinstance(v, list):
            raise ValueError("tags must be a list of strings")
        
        # Sanitize: strip whitespace and ignore empty elements
        sanitized = [tag.strip() for tag in v if isinstance(tag, str) and tag.strip()]
        
        # Validation checks
        if len(sanitized) > 5:
            raise ValueError("cannot have more than 5 tags")
        for tag in sanitized:
            if len(tag) > 20:
                raise ValueError("tag length cannot exceed 20 characters")
        return sanitized


class TaskUpdate(BaseModel):
    """
    Schema for partial updates of an existing task.
    Accepts: title (optional), description (optional), status (optional for transitions), 
    priority (optional), assignee (optional), tags (optional).
    Rejects: id, created_at, updated_at (server-managed).
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=2000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    assignee: Optional[str] = Field(default=None, max_length=255)
    tags: Optional[List[str]] = Field(default=None)

    model_config = ConfigDict(extra="forbid")

    @field_validator("title", mode="before")
    @classmethod
    def validate_title_not_blank(cls, v: Optional[str]) -> Optional[str]:
        """If title is provided, it must not be empty or whitespace-only."""
        if v is not None:
            if isinstance(v, str):
                stripped = v.strip()
                if not stripped:
                    raise ValueError("title cannot be empty or whitespace-only")
                return stripped
            raise ValueError("title must be a string")
        return None

    @field_validator("tags", mode="before")
    @classmethod
    def validate_tags(cls, v: Optional[List[str]]) -> Optional[List[str]]:
        """If tags are provided, validate they are formatted correctly."""
        if v is None:
            return None
        if not isinstance(v, list):
            raise ValueError("tags must be a list of strings")
        
        sanitized = [tag.strip() for tag in v if isinstance(tag, str) and tag.strip()]
        
        if len(sanitized) > 5:
            raise ValueError("cannot have more than 5 tags")
        for tag in sanitized:
            if len(tag) > 20:
                raise ValueError("tag length cannot exceed 20 characters")
        return sanitized


class TaskResponse(BaseModel):
    """
    Complete task as returned by the API.
    Includes server-generated id, status, created_at, updated_at.
    """
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    priority: TaskPriority
    assignee: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)