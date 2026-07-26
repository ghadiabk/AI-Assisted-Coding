# Final AI Review and Ownership Evidence

## AGENTS.md guardrails
- Repo-specific stack and commands included: **yes**
- Docs-first/read-first guardrail included: **yes**
- Unexpected app/frontend edits rule included: **yes**

## AI code review mini-log

| AI comment | Grade: Useful / Noise / Wrong | Reason | Verification or decision |
|---|---|---|---|
| "Missing status transition check on batch edits" | **Useful** | AI identified that updating status alongside title could bypass validation if status wasn't evaluated first. | Fixed logic in `app/main.py` so transition checks run before secondary field updates. |
| "Change type hints from List[str] to Sequence[str]" | **Noise** | Technically valid for immutability, but unnecessary overhead for our lightweight FastAPI app. | Ignored. Retained `List[str]`. |
| "TaskUpdate model should allow user to edit task ID" | **Wrong** | `id` is a server-managed field and must remain forbidden on client update payloads (`extra="forbid"`). | Rejected. Maintained `extra="forbid"` in Pydantic schema. |

## AI security mini-review

| Finding | File evidence | Grade: Valid / False Positive / Noise | Reason | Next action |
|---|---|---|---|---|
| Unbounded tag array input | `app/models/task.py` | **False Positive** | AI missed that `@field_validator("tags")` caps tags at 5 items max and 20 chars each. | None. Documented existing validator. |
| Missing authentication on task endpoints | `app/main.py` | **Valid** | Accurate finding for a production environment, though an intentional scope boundary for this course. | Documented in Top-3 backlog for future iterations. |
| CORS allows local dev origins | `app/main.py` | **Noise** | Allowing `localhost:5500` is expected for local frontend development. | Retained CORS settings for local dev. |

## Manual security check
I manually inspected `app/storage/tasks.py` and confirmed that unhandled exception responses on malformed JSON payloads return Pydantic stack trace details in the response body. This exposes schema validation internal structures, which should be caught with a global exception handler before production deployment.

## One AI output I rejected or corrected
The AI originally generated `setupDragAndDrop()` using `.addEventListener('drop', ...)`. Because `renderBoard()` was called repeatedly on updates, duplicate drop listeners accumulated. Dragging a card triggered multiple PATCH requests, causing subsequent duplicate requests to fail with HTTP 422 (same-to-same transition). I rejected the AI's code and replaced `.addEventListener()` with direct property assignment (`element.ondrop = ...`) to overwrite listeners on each render.

## Three AI usage rules
1. **Never paste:** I will never paste `.env` files, production database credentials, API tokens, user PII, or real customer data into an AI tool.
2. **Always verify:** Before accepting any AI-generated code diff, I will read every line changed and run `pytest tests/ -v` or verify browser behavior locally.
3. **Record AI contributions by:** Documenting the prompt intent, the accepted code diff, and the specific verification test run in PR descriptions or commit logs.

## Ownership statement
I am comfortable submitting this repository as my own work because I initiated every prompt, reviewed every line of generated code, and verified runtime correctness using local tests and Docker builds. Where the AI generated incorrect code—such as accumulating event listeners or omitting endpoint parameters—I diagnosed the root cause, rejected the invalid suggestions, and wrote the fixes myself. I understand the architecture, business logic, and test coverage of this codebase completely.