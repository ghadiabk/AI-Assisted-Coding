# Feature Plan & Critique: Task Comments

## Proposed Scope
Add the ability to post, view, and delete text comments on individual tasks.

---

## Repo-Grounded Plan Critique

### 1. Data Model (`app/models/task.py`)
* **Plan:** Create a `TaskComment` Pydantic model with `id` (int/str), `task_id` (int), `author` (str, 1-100 chars), `body` (str, 1-2000 chars), and `created_at` (datetime).
* **Critique:** **Right.** Aligns with existing Pydantic v2 patterns and field constraints in the codebase.

### 2. Storage Layer (`app/storage/tasks.py`)
* **Plan:** Store comments in a global dictionary `_comments: Dict[int, List[dict]]` keyed by `task_id`.
* **Critique:** **Right.** Extends the existing in-memory dictionary pattern without introducing database overhead.

### 3. API Endpoints (`app/main.py`)
* **Plan:** 
  * `POST /tasks/{task_id}/comments` -> Creates comment (returns 201).
  * `GET /tasks/{task_id}/comments` -> Lists comments for task (returns 200).
* **Critique:** **Needs-Resequencing.** The plan places frontend integration before defining the error handling for `POST` on a non-existent `task_id` (which must return 404 first).

### 4. Testing Plan (`tests/test_tasks.py`)
* **Plan:** Add unit tests for valid comment creation, missing task IDs (404), and blank body rejection (422).
* **Critique:** **Right.** Matches our current pytest fixture setup and Break Test procedures.

---

## Comparison: Generic Plan vs. Repo-Grounded Plan

1. The **generic plan** assumed an SQL database with SQLAlchemy foreign keys and an OAuth user session model that does not exist in this project.
2. The **repo-grounded plan** correctly identified our `app/storage/tasks.py` in-memory structure and Pydantic v2 conventions.
3. A generic plan is sufficient for initial product brainstorming, but a repo-grounded plan is mandatory before writing implementation prompts.