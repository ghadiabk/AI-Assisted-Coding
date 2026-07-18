# Task Tracker - Architecture Decision Record (ADR)

## Architecture Decision

**Chosen:** FastAPI + in-memory JSON storage for Module 1

This is a learning project focused on the AI-assisted development workflow, not production deployment. I chose FastAPI with in-memory task storage (Python dict) backed by JSON file persistence, rather than a database, because it meets all four evaluation criteria for this scope. Simplicity is maximized: the entire data layer fits in ~50 lines, uses only the Python standard library, and requires no external database setup or migration tooling. Testability is straightforward—tasks are pure Python objects, mocking is trivial, and no database state needs cleaning between tests. Local deployability is immediate: one `pip install` and `uvicorn` command gets the server running without Docker, environment variables, or infrastructure setup. Familiarity is high: FastAPI and standard JSON I/O are approachable for a learning context. I explicitly rejected AI suggestions to add SQLAlchemy/SQLModel (adds complexity too early), async Celery tasks (out of scope), and Docker Compose (hides the actual application under orchestration). If this project grows to multi-user, concurrent writes, or persistent data requirements, the risk is that the JSON file approach will fail: concurrent PATCH requests could lose data, and scaling to thousands of tasks will degrade file I/O performance. At that point, I would migrate to SQLite and a proper ORM, but that's a Module 2+ decision.

---

## Key Architecture Decisions

| Aspect | Decision | Reasoning |
|--------|----------|-----------|
| **Framework** | FastAPI | Type hints, automatic validation, built-in Swagger docs |
| **Data Storage** | In-memory dict + JSON file | Simple, no infrastructure, testable, file-backed for persistence |
| **API Style** | RESTful JSON | Matches requirements; stateless endpoints |
| **Validation** | Pydantic models | Leverages FastAPI, automatic error 422 responses |
| **Testing** | pytest + TestClient | Standard FastAPI testing pattern |
| **Project Structure** | Modular (routes, models, core) | Scalable, supports moving to DB later |

---

## Rejected Architecture Options

### Option 1: FastAPI + SQLModel/SQLAlchemy
- **AI suggested this** to be "more realistic"
- **Why rejected:** Adds connection pooling, migration files, and ORM learning curve that obscure the AI workflow. SQLite can be added in 30 minutes when needed, but right now it's premature complexity.

### Option 2: FastAPI + Docker Compose
- **AI suggested this** for "production readiness"
- **Why rejected:** Docker adds a container layer that hides what the application actually does. Running Uvicorn directly teaches more.

---

## Risks and Growth Path

| Risk | Mitigation | When to Address |
|------|-----------|-----------------|
| **Concurrent writes to JSON file** | Requests will overwrite each other if two PATCH requests hit simultaneously. | When multi-user concurrency is a requirement (Module 2+) |
| **File I/O performance** | Grows slower with large task lists (1000+ tasks). | When task list exceeds 10K items |
| **No query indexing** | Filtering by status requires scanning all tasks. | When performance profiling shows filtering is a bottleneck |

**Growth path:** 
- Module 1: In-memory + JSON file (learning focus)
- Module 2: Migrate to SQLite with SQLModel (persistence without complexity)
- Module 3+: Add authentication, real-time updates, cloud deployment

---

## Assumptions Documented

✅ **Assumption made in design:** Assuming single-user or non-concurrent usage  
✅ **Assumption made in design:** Assuming task list stays under 10K items  
✅ **Assumption made in design:** Assuming no multi-tenancy or per-user isolation needed

