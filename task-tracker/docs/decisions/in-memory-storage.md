# Decision Note: In-Memory Dictionary with JSON Persistence for Task Storage

## Context
During the initial architectural setup, we needed a lightweight storage mechanism to support rapid prototyping, unit testing, and prompt engineering exercises without introducing database migrations or external dependencies.

## Decision
We decided to store tasks in a global Python dictionary (`Dict[int, dict]`) in `app/storage/tasks.py`, synchronized to a local `tasks.json` file on file mutation operations.

## Alternatives Considered
1. **SQLite with SQLModel/SQLAlchemy:** Would provide relational schema enforcement and persistent disk storage.
2. **Pure In-Memory (No Persistence):** Simple for pytest runs, but loses data whenever Uvicorn reloads.

## Trade-offs
* **Benefits:** Zero setup required, fast test execution, simple debugging, no external database service required.
* **Drawbacks:** Not thread-safe for concurrent multi-user environments, inefficient filtering at large scale ($O(N)$ list scans), potential file corruption on abrupt server termination.

## Consequences
All CRUD helper operations (`add_task`, `update_task`, etc.) operate synchronously on the in-memory `_tasks` dictionary and trigger `_save_to_file()`. State isolation across unit tests is handled via an autouse fixture calling `_reset()`.

## Open Questions
How will we handle database migrations when migrating to PostgreSQL or SQLite in future iterations?

---

> "I would do this differently if this application were intended for concurrent production traffic, where I would immediately replace file persistence with an async PostgreSQL database and SQLAlchemy ORM."