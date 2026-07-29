# Personal AI Engineering Playbook

## 1. Operating Rules

### When I reach for AI first
* Generating initial boilerplate, file structures, and repetitive test scenarios.
* Explaining unfamiliar stack traces, error outputs, or framework conventions.
* Drafting initial Markdown documentation outlines and user story templates.

### When I DO NOT reach for AI first
* Designing core business logic and state machine transition matrices.
* Evaluating security boundaries, access controls, or credential handling.
* Approving PR diffs or deciding whether code is ready for production merge.

### My Non-Negotiables
* **Never Paste:** I will never paste `.env` keys, tokens, credentials, or production database payloads into an AI tool.
* **Always Run:** I will never accept an AI code diff without running `pytest` or verifying browser behavior locally first.
* **Break Test Proof:** I will verify new tests by deliberately breaking source code to confirm the test fails before accepting it as green.

### My review rules
* Read the diff before approving any file edits.
* Triage AI code review comments into Useful, Noise, or Wrong before making code edits.
* Reject any AI output that suppresses error symptoms instead of fixing root causes.

### What I am still figuring out
* How to best configure repository context limits for larger multi-service codebases without overwhelming the AI context window.
* When to transition from lightweight in-memory storage prototyping to a full relational database model during early-stage development.

---

## 2. Decision Card

| Category | My Choice & Workflow | Evidence / Rationale |
|---|---|---|
| **New Feature** | IDE Chat (Cursor / Copilot) with file references | File-aware context prevents hallucinated module imports. |
| **Code Review** | Read-only Terminal Agent / Desktop Workspace | Triage feedback into Useful, Noise, or Wrong before making edits. |
| **Debugging** | Paste exact failing test name and full stack trace | Vague prompts produce generic advice; exact stack traces yield precise fixes. |
| **Infrastructure** | Multi-stage Dockerfile + `.dockerignore` static review | Explicit slim bases and non-root users must be verified manually (`whoami`). |
| **Never Paste** | Secrets, API keys, `.env` files, user PII, production logs | Exclude via `.gitignore` and enforce strict negative prompt rules. |
| **One Rule** | *"AI drafts, but the human inspects, tests, and owns the final diff."* | Proven in Module 3 when AI generated duplicate event listener memory leaks. |

---

## 3. Reflection & 30-Day Reminder

> *"I would do this differently if I were relying solely on automated AI outputs without local test suites, as silent logic bugs (like un-sanitized array inputs or missing transition checks) would easily bypass un-verified reviews."*

* **30-Day Calendar Reminder Set:** `Re-read docs/ai-playbook.md and evaluate: Am I still following these rules?`