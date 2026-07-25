# CLAUDE.md - Task Tracker Project Context

## Project Overview
Task Tracker is a lightweight REST API built with FastAPI and a Vanilla JS frontend Kanban board.

## Tech Stack
* **Backend:** Python 3.12, FastAPI, Pydantic v2, Uvicorn
* **Frontend:** Vanilla HTML5 / CSS3 / JavaScript (ES6+), Native Drag-and-Drop
* **Testing:** pytest, httpx (TestClient)
* **Storage:** In-memory dictionary with local `tasks.json` file persistence

## Common Developer Commands
* **Run Server:** `uvicorn app.main:app --reload --port 8000`
* **Run Tests:** `pytest tests/ -v`
* **Run Single Test:** `pytest tests/ -k "<test_name>" -v`
* **Format & Lint:** `flake8 app/` (if configured)

## Architecture & Code Map
* `app/main.py`: FastAPI routes, CORS configuration, query filters (`status`, `priority`, `search`, `tag`).
* `app/models/task.py`: Pydantic v2 models (`TaskCreate`, `TaskUpdate`, `TaskResponse`) with `@field_validator`.
* `app/storage/tasks.py`: In-memory data store with JSON persistence and reset logic (`_reset`).
* `app/business_rules.py`: Status transition matrix validation (`validate_status_transition`).
* `frontend/index.html`: Kanban UI layout, modal handlers, debounced search filtering.
* `tests/test_tasks.py`: Test suite for API routes, validation errors, and transition edge cases.

## Core Business Rules
1. **Task Statuses:** `ToDo`, `InProgress`, `Done`.
2. **Allowed Transitions:**
   * `ToDo` -> `InProgress`
   * `InProgress` -> `Done`
   * `Done` -> `InProgress` (Reopening)
3. **Disallowed Transitions:**
   * `ToDo` -> `Done` (Cannot skip `InProgress`)
   * `Done` -> `ToDo` (Cannot revert to start)
   * Same-status -> Same-status (No-op moves rejected with 422)
4. **Validation Limits:** Title required (1–200 chars, no blank whitespace). Max 5 tags, max 20 chars per tag.

## Do-Not Rules (Negative Constraints)
* **DO NOT** introduce external database ORMs (SQLAlchemy/SQLModel) unless explicitly requested.
* **DO NOT** add authentication or multi-user tenancy.
* **DO NOT** use `continue-on-error`, `|| true`, or `--exit-zero` in CI pipelines.