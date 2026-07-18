# Reflection Log - Module 1 Task Tracker

## Part A: Requirements Generation

**What AI got right:**
- Generated well-structured user stories with clear "As a / I want / So that" format
- Included acceptance criteria for each story
- Identified key operations: create, view, filter, update, delete
- Recognized the need for validation and error handling

**What I corrected:**
- **Status transitions:** AI initially allowed any status update. I added business logic that Done is terminal—tasks cannot move back to InProgress or ToDo.
- **Enum constraints:** AI suggested free-form string fields for status and priority. I enforced enum validation (ToDo/InProgress/Done and Low/Medium/High).
- **Whitespace handling:** AI missed the requirement to trim and validate whitespace-only titles. Added explicit trimming validation.
- **Required fields:** AI made priority optional; I made it required based on the task structure.
- **Delete response codes:** AI forgot to specify 404 for missing tasks on delete. I clarified 404 should be returned.

**Assumption AI made:**
- AI assumed a simple happy-path implementation without considering edge cases like concurrent updates, idempotency, or state machine constraints for status transitions.

---

## Part B: Architecture Decision

**What AI got right:**
- Suggested FastAPI as appropriate for a lightweight REST API
- Recognized that in-memory storage is suitable for learning projects
- Identified that JSON file persistence provides a simple backup mechanism
- Noted trade-offs explicitly (simple vs. realistic)

**What I corrected:**
- **Database suggestion:** AI wanted to add SQLAlchemy/SQLModel immediately "for realism." I rejected this; the project is about the AI workflow, not production systems. Clarity on exclusions prevents scope creep.
- **Docker addition:** AI suggested Docker Compose "for production readiness." I rejected it; Docker adds complexity that hides what the application actually does.
- **Async tasks:** AI suggested Celery for background jobs. Out of scope for Module 1.

**Assumption AI made:**
- AI defaulted to "what real systems do" rather than respecting the learning-first scope. The assumption was that educational projects should mimic production to have value.

---

## Part C: Scaffold Execution

**What AI got right:**
- Generated clean FastAPI app structure with proper app factory pattern
- Pydantic models with correct validation decorators
- Proper enum usage for Status and Priority
- JSON file storage with load/save logic
- Correct HTTP status codes and response shapes
- Modular structure (routes, models, storage, core folders) that supports future growth

**What I corrected:**
- **Validator placement:** AI generated validators but didn't trim whitespace in the model. I ensured the validator strips and validates.
- **File persistence:** AI's save logic didn't handle concurrent writes. For Module 1 scope, this is acceptable, but I documented it as a risk for the ADR.
- **Status transitions:** Storage layer had no business logic for state machine. I added `update_task_status()` function that validates transitions and prevents Done → ToDo/InProgress.

**Assumption AI made:**
- AI assumed all fields should be stored directly without normalization (e.g., didn't trim whitespace on input). The model validation catches it, but the assumption was "store what was sent."

---

## Key Learning: The Interaction Loop in Action

### Ask → Inspect → Run → Test → Refine

1. **Ask:** Clear structured prompt for requirements with role/context, task, constraints, and output format
2. **Inspect:** Read generated stories and caught missing business rules (status transitions, enum constraints)
3. **Run:** Scaffolded code, created project structure, installed dependencies
4. **Test:** Verified /health endpoint, root endpoint, and Swagger docs all return 200 and correct responses
5. **Refine:** Documented corrections and why they matter

This loop prevents accepting AI output too quickly and builds the habit of deliberate review.

---

## What I'd Do Next (Module 2)

1. **Implement CRUD endpoints** for tasks
2. **Add comprehensive testing** with pytest
3. **Integrate SQLite** for persistent storage
4. **Add authentication** (simple token-based, not OAuth yet)
5. **Create basic frontend** (HTML/CSS form or React)

---

## Habits Reinforced

✅ **AI is a junior collaborator:** It drafted quickly but missed business rules and made scope assumptions.  
✅ **Review deliberately:** Two major assumptions caught before implementation (status transitions, enum fields).  
✅ **Constraints prevent hallucination:** Explicit "no auth, no external database, no Docker" kept the scope tight.  
✅ **Simple projects, serious workflow:** The intentional simplicity (JSON file storage) made the AI interaction loop visible and educational.  

---

## File Manifest

- `REQUIREMENTS.md` - Reviewed user stories with corrections documented
- `ARCHITECTURE.md` - ADR with rejected options and risk analysis
- `app/main.py` - FastAPI app with /health and / endpoints
- `app/models/task.py` - Pydantic models with enum validation
- `app/storage/tasks.py` - In-memory storage with state machine logic
- `requirements.txt` - Python dependencies
- `README.md` - Setup and run instructions
- `.env.example` - Environment variables template
- `.gitignore` - Standard Python ignores
- `REFLECTION_LOG.md` - This file

---

## Running the Project

```bash
cd task-tracker
python -m venv venv
# On Windows: .\venv\Scripts\python.exe -m uvicorn app.main:app --reload
# On macOS/Linux: source venv/bin/activate && uvicorn app.main:app --reload
```

Then visit:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health
