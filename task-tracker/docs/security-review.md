# Task Tracker Security Review & Audit Reconciliation

## 1. AI Findings Grading Table

| # | AI Finding | File Evidence | Risk Description | Grade | Rationale |
|---|---|---|---|---|---|
| 1 | Unbounded tag array input | `app/models/task.py` | Allowing unlimited tags could exhaust server memory. | **False Positive** | The AI missed that `@field_validator("tags")` limits tags to a max of 5 items and 20 chars each. |
| 2 | Missing authentication on endpoints | `app/main.py` | Anyone can create, edit, or delete tasks without credentials. | **Valid** | Accurate finding for a production app, though this is an intentional scope boundary for this learning project. |
| 3 | CORS configuration allows local origins | `app/main.py` | `allow_origins` includes local dev ports (`5500`, `8000`). | **Noise** | Technically true, but standard and expected for local development environments. |
| 4 | Potential SQL Injection in task filtering | N/A | Malicious string payloads could compromise database queries. | **False Positive** | The AI hallucinated an SQL backend; our project uses pure in-memory Python dictionaries. |

---

## 2. Manual Security Findings (Human Audit)

| # | Finding | File Evidence | Risk Description |
|---|---|---|---|
| M1 | Unbounded `description` field in storage | `app/models/task.py` | `description` allows up to 2000 characters, but storing thousands of large strings in `_tasks` memory without cleanup can cause memory pressure over time. |
| M2 | Unhandled exception details on invalid JSON | `app/main.py` | Sending malformed JSON payloads returns Pydantic stack trace details in the response body, exposing internal validation schema structures. |

---

## 3. Reconciliation Matrix

| Agreement (AI & Human) | AI-Only Findings | You-Only Findings (Human Judgment) |
|---|---|---|
| Missing endpoint authentication/authorization | CORS local origin warnings (Noise) | Unhandled validation exception response leaks |
| | SQL Injection hallucination (False Positive) | In-memory dict size growth risk under sustained payloads |

---

## 4. Top-3 Security Backlog

1. **Implement Token-Based Authentication:** Restrict `POST`, `PATCH`, and `DELETE` endpoints to authenticated headers before deploying outside local dev.
2. **Sanitize Exception Responses:** Catch raw Pydantic validation errors globally to prevent exposing schema structures in API responses.
3. **Cap Overall Storage Count:** Implement an upper boundary limit in `app/storage/tasks.py` (e.g., max 10,000 tasks) to protect against memory exhaustion.