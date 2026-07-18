# Task Tracker - User Stories (Module 1)

## User Stories Table

| ID | Story | Acceptance Criteria | Notes / Assumptions |
|---|---|---|---|
| US-01 | As a team member, I want to create a new task with title, description, priority, and assignee so that I can add work to the task list | 1. POST /tasks accepts title (required), description (optional), priority, and assignee fields in JSON<br/>2. New task is assigned status "ToDo" by default<br/>3. Created task is immediately visible in the task list (GET /tasks) | Title is required and must be non-empty after trimming whitespace. Priority (Low/Medium/High) is required; assignee is optional. |
| US-02 | As a team member, I want to view all tasks in a single list so that I can see everything that needs to be done | 1. GET /tasks returns all tasks as a JSON array<br/>2. Each task includes id, title, description, status, priority, and assignee<br/>3. Empty task list returns [] not null; HTTP 200 in both cases | Returns tasks in insertion order. No sorting or pagination in Module 1. |
| US-03 | As a team member, I want to filter tasks by status (ToDo, InProgress, Done) so that I can focus on work in a specific stage | 1. GET /tasks?status=ToDo returns only tasks with status "ToDo"<br/>2. Valid status values are "ToDo", "InProgress", "Done"; invalid values return HTTP 422 with error message<br/>3. Filtering returns correct count of matching tasks | Only one status filter per request in Module 1. Case-sensitive status values. |
| US-04 | As a team member, I want to filter tasks by priority (Low, Medium, High) so that I can focus on high-impact work first | 1. GET /tasks?priority=High returns only tasks with priority "High"<br/>2. Valid priority values are "Low", "Medium", "High"; invalid values return HTTP 422 with error message<br/>3. Filters work independently; filtering by both status and priority combines constraints | Priority filter returns correct subset. Returns empty list if no matches (not null or error). |
| US-05 | As a team member, I want to update task details (title, description, priority, assignee) so that I can keep task information current as requirements evolve | 1. PATCH /tasks/:id accepts title, description, priority, assignee as optional fields<br/>2. Only provided fields are updated; omitted fields remain unchanged<br/>3. Returns HTTP 404 if task id does not exist; returns HTTP 422 if provided values are invalid | Title validation: non-empty after trimming, max 255 chars. Partial updates supported. |
| US-06 | As a team member, I want to move a task through workflow stages (ToDo → InProgress → Done) so that I can track work progress | 1. PATCH /tasks/:id/status with new_status in body transitions the task to the new status<br/>2. Valid transitions: ToDo→InProgress, InProgress→Done<br/>3. Done tasks cannot transition back; attempting to do so returns HTTP 400 with reason "Done status is terminal" | Status is moved through a controlled workflow. Only forward progress allowed for Done. Returns clear error for invalid transitions. |
| US-07 | As a team member, I want to delete a completed or obsolete task so that the task list stays focused and clean | 1. DELETE /tasks/:id removes the task from the list<br/>2. Returns HTTP 204 (No Content) on success<br/>3. Returns HTTP 404 if task id does not exist; deleted task no longer appears in GET /tasks results | Deletion is permanent. No undo in Module 1. Immediately visible in subsequent GET requests. |
| US-08 | As a team member, I want the API to validate task data (empty titles, invalid statuses/priorities) so that invalid data does not corrupt the task list | 1. Empty title ("") and whitespace-only title ("   ") are both rejected with HTTP 422 and descriptive error<br/>2. Invalid status or priority values are rejected with HTTP 422 before task is modified<br/>3. All validation errors include a clear message describing what failed | Validation happens before write. Error response includes field name and reason. Title trimming applied before validation. |

---

## Story Mapping to Features

| Feature | Stories | Coverage |
|---------|---------|----------|
| **Create** | US-01 | Happy path: create with all fields |
| **View** | US-02 | Happy path: list all tasks |
| **Filter** | US-03, US-04 | Both status and priority filters; invalid filter values covered |
| **Update Details** | US-05 | Partial updates; validation; 404 handling |
| **Update Status** | US-06 | Controlled transitions; Done is terminal; invalid transitions return 400 |
| **Delete** | US-07 | Happy path; 404 handling; permanent removal |
| **Validation** | US-08 | Cross-cutting concern; covers whitespace, invalid enums, error messages |

---

## Failure Cases Covered

| Failure Mode | Story | Acceptance Criterion |
|---|---|---|
| Missing/empty title | US-01, US-08 | Title validation rejects empty and whitespace-only strings |
| Invalid status value | US-03, US-08 | Invalid status returns 422 with error message |
| Invalid priority value | US-04, US-08 | Invalid priority returns 422 with error message |
| Task not found | US-05, US-07 | Attempting to PATCH/DELETE non-existent task returns 404 |
| Invalid status transition | US-06 | Attempting to move Done task back returns 400 with "terminal" message |

---

## Notes for Development Team

### Context Block (for AI prompts)
```
I am building a Task Tracker REST API using Python and FastAPI.
The app supports create, view, update, and delete operations for tasks.
Each task has id, title, description, status (ToDo/InProgress/Done), priority (Low/Medium/High), and assignee.
No authentication, no database yet (in-memory storage with JSON file backup).
I am using the loop: ask, inspect, run, test, refine.
```

### Acceptance Criteria Emphasis
- All AC should be **testable with curl or test client**, not subjective ("looks good")
- Status codes matter (422 for validation, 404 for not found, 204 for delete success, etc.)
- Error messages must be **descriptive** (not "Invalid input")
- Edge cases like whitespace-only strings are explicitly included

### Excluded (Don't Add)
- Authentication / user accounts
- Multi-tenancy or per-user lists
- Real-time updates or WebSockets
- Mobile app or responsive design requirements
- Database specifics; in-memory storage is acceptable
- Email notifications, webhooks, or integrations

### Module 1 Scope
These stories are sized for a **minimal 1-2 day sprint** to establish:
- Working endpoints
- Pydantic validation
- JSON file persistence
- Swagger API docs
- Basic test coverage

Pagination, sorting, bulk operations, and advanced filtering are **Module 2+**.

---

## AI Interaction Notes

### When Prompting for Implementation
Use this refined prompt structure:

**Role/Context:**
> You are a senior FastAPI developer implementing REST endpoints for task management.

**Task:**
> Implement the POST /tasks endpoint for story US-01. Requirements: accept title (required), description (optional), priority, assignee; assign status "ToDo"; return 201 with created task including auto-generated id.

**Constraints:**
> - Use Pydantic for validation
> - Title must be non-empty after trimming whitespace
> - Return 422 with descriptive error if title is empty or priority is invalid
> - Do not implement authentication or persistence layer yet; assume in-memory storage

**Output format:**
> Return only the endpoint function. No explanation or additional boilerplate.

This specificity prevents AI from adding auth, database, logging, or other out-of-scope extras.

