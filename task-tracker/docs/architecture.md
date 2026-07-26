# Task Tracker System Architecture

## System Overview
Task Tracker is an asynchronous REST API built with FastAPI and served via Uvicorn, accompanied by a single-page Vanilla JS Kanban board frontend.

## Backend Structure & Component Map
* `app/main.py`: Entry point configuring FastAPI, CORS middleware, CRUD endpoints, and multi-parameter query filtering (`status`, `priority`, `search`, `tag`).
* `app/models/task.py`: Data validation boundary using Pydantic v2 schemas (`TaskCreate`, `TaskUpdate`, `TaskResponse`).
* `app/storage/tasks.py`: Synchronous in-memory store (`_tasks`) with JSON file backup (`tasks.json`).
* `app/business_rules.py`: Encapsulates workflow state machine rules (`validate_status_transition`).

## Data Flow Pipeline
1. **Client Request:** Browser or HTTP client sends JSON payload to an endpoint (e.g. `POST /tasks`).
2. **Schema Validation:** Pydantic models validate constraints (title non-blank, max 5 tags) and raise HTTP 422 on failure.
3. **Business Logic Execution:** Status updates pass through `validate_status_transition()`. Invalid transitions raise HTTP 422.
4. **Storage & Persistence:** In-memory `_tasks` dictionary updates and immediately triggers `_save_to_file()`.
5. **Response:** Sanitized `TaskResponse` returned with HTTP status code (201 for create, 200 for update, 204 for delete).

## Known System Boundaries
* **In-Memory Storage:** Non-thread-safe synchronous file persistence designed for single-instance learning environments.
* **Authentication:** Excluded by design; endpoints are publicly accessible.

---

## Context Strategy Comparison Log & Rule

* **Strategy A (Minimal):** Produced fluent but generic text that hallucinated a PostgreSQL database and missing auth middleware.
* **Strategy B (Structured):** Accurately described the folder structure but added unnecessary boilerplate sections.
* **Strategy C (Targeted):** Highly precise on file paths, Pydantic validators, and exact route status codes. Refused to guess unprovided details.

> **Context Strategy Rule:**  
> *"For architecture and verification tasks, use **Targeted Context (Strategy C)** by attaching exact anchor files, because limiting the model's visibility forces honest, precise statements and prevents hallucinated infrastructure."*