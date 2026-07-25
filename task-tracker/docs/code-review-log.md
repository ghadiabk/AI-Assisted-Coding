# AI Code Review Triage Log

## Personal AI Review Rule
> "I will use AI reviews for quick syntactic coverage, but I will manually verify every reported issue against running code before taking action."

---

## Review Comment Categorization

### 1. Comment: "Missing status transition check on batch edits"
* **Category:** Useful
* **Justification:** The AI noted that updating status alongside title could bypass validation if status wasn't checked first.
* **Action Taken:** Fixed logic in `app/main.py` so transition checks run before secondary field updates.

### 2. Comment: "Consider changing type hints from List[str] to Sequence[str]"
* **Category:** Noise
* **Justification:** Technically valid for immutable inputs, but unnecessary for our lightweight FastAPI codebase.
* **Action Taken:** Ignored.

### 3. Comment: "TaskUpdate model should allow id parameter"
* **Category:** Wrong
* **Justification:** `id` is a server-generated field and must remain forbidden on client update payloads (`extra="forbid"`).
* **Action Taken:** Rejected. Added explicit negative constraint to `CLAUDE.md`.