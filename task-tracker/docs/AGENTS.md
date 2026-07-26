# AGENTS.md - Repository Instructions & Module 5 Guardrails

## Tech Stack & Core Commands
* **Stack:** Python 3.12, FastAPI, Pydantic v2, Uvicorn, pytest, httpx, Vanilla JS frontend.
* **Server Command:** `uvicorn app.main:app --reload --port 8000`
* **Test Command:** `pytest tests/ -v`
* **Docker Commands:** `docker build -t task-tracker:dev .` / `docker run --rm -p 8000:8000 task-tracker:dev`

## Architecture & Project Rules
* `app/main.py`: Route handlers, CORS middleware, and query parameter filtering (`status`, `priority`, `search`, `tag`).
* `app/models/task.py`: Pydantic v2 schemas (`TaskCreate`, `TaskUpdate`, `TaskResponse`).
* `app/storage/tasks.py`: Synchronous in-memory store with `tasks.json` file backing and test reset helper `_reset()`.
* `app/business_rules.py`: Status transition validation logic.

## Business Rule Matrix
* Valid status transitions: `ToDo` -> `InProgress`, `InProgress` -> `Done`, `Done` -> `InProgress`.
* Invalid status transitions: `ToDo` -> `Done`, `Done` -> `ToDo`, and same-to-same transitions (e.g. `ToDo` -> `ToDo`).
* Field constraints: Title required (1-200 chars, non-blank). Tags optional (max 5 tags, max 20 chars per tag).

## Module 5 Strict Boundaries
1. **Read-Only / Documentation Focus:** Prefer read-only analysis. Required output must be markdown files placed inside `docs/`.
2. **Reject Code Edits:** Reject any proposed modifications to `app/` or `frontend/` unless explicitly instructed for a minor security fix.
3. **Evidence Requirement:** Every claim about application behavior must cite specific file names and line numbers.