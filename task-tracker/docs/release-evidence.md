# Release Evidence

## Baseline
- **Branch:** `final-project`
- **Date:** October 2024
- **Local app run command:** `uvicorn app.main:app --reload --port 8000`
- **`/health` result:** HTTP 200 `{"status": "ok", "timestamp": "2024-10-24T12:00:00+00:00"}`
- **Frontend check:** Confirmed Kanban board renders columns (To Do, In Progress, Done), cards sort by priority, drag-and-drop moves cards, and create/edit modal functions without errors.
- **Test command:** `pytest tests/ -v`
- **Test result:** 36 passed in 0.25s

## CI evidence
- **Workflow file:** `.github/workflows/ci.yml`
- **Latest run status:** Passing (Green checkmark on GitHub Actions)
- **Test command used by CI:** `pytest tests/ -v`
- **Shortcut check:** Verified: No `continue-on-error`, no `|| true`, pytest command is not skipped, explicit Python 3.12 version configured.

## Docker evidence
- **Build command:** `docker build -t task-tracker:dev .`
- **Run command:** `docker run --rm -d -p 8000:8000 --name tt-dev task-tracker:dev`
- **`/health` check:** `curl -i http://localhost:8000/health` returned HTTP 200 OK.
- **Non-root check:** `docker exec tt-dev whoami` returned `appuser`.
- **No-baked-secrets check:** `.dockerignore` explicitly excludes `.env`, `tasks.json`, `.git`, and test caches.

## Documentation claim-vs-reality log

| Claim checked | Evidence used | Result | Change made, if any |
|---|---|---|---|
| "POST /tasks returns HTTP 200" | `app/main.py` code inspection | Inaccurate | Updated docstrings and README to explicitly state `201 Created`. |
| "DELETE /tasks/{id} returns JSON object" | `app/main.py` route decorator | Inaccurate | Updated docstrings to show `204 No Content` with an empty response body. |
| "Status can transition freely across any state" | `app/business_rules.py` matrix | Inaccurate | Rewrote documentation to accurately explain allowed transitions (`ToDo` -> `InProgress` -> `Done` -> `InProgress`). |