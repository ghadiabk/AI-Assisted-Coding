# Mid-Course Project: User Stories

## Feature 1: Tags & Labels

### US-T1: Create and Edit Tasks with Tags
* **As a** team member,
* **I want to** attach comma-separated tags when creating or editing a task,
* **So that** I can categorize tasks by topic or project domain.

* **Acceptance Criteria:**
  1. The task modal includes a text field for comma-separated tags.
  2. Tags are saved as a list of trimmed strings.
  3. Empty tag entries resulting from trailing or duplicate commas (e.g., `bug, , urgent`) are removed automatically.
  4. Entering more than 5 tags returns an HTTP 422 validation error.
  5. Entering a tag exceeding 20 characters returns an HTTP 422 validation error.

* **AI Assumption Corrected:** The AI originally suggested creating a separate SQL database table and relational mapping for tags. I corrected this assumption to maintain our simple in-memory architecture, storing tags as a native string array (`List[str]`) directly on the task object.

---

### US-T2: Visual Tag Displays on Kanban Cards
* **As a** board user,
* **I want to** see tags rendered as visual chips on each task card,
* **So that** I can scan task categories without opening the edit modal.

* **Acceptance Criteria:**
  1. Each tag is displayed as a styled `.tag-chip` element on the card.
  2. If a task has no tags, no tag container is rendered, avoiding unnecessary spacing.
  3. Tags are rendered in lowercase for visual consistency.

---

### US-T3: Preserve Tags on Unrelated Detail Updates
* **As a** team member,
* **I want** existing tags to remain unchanged when I update other fields like title or priority,
* **So that** saving an edit does not accidentally clear a task's tags.

* **Acceptance Criteria:**
  1. Submitting a `PATCH /tasks/{id}` request with fields like `priority` or `title` preserves existing `tags` if `tags` is omitted or unchanged in the request.
  2. Updating tags explicitly replaces the existing tag array with the new list.

* **AI Assumption Corrected:** The AI initially omitted `tags` from the `PATCH` handler parameters in `app/main.py`, which caused tag updates to be discarded. I updated the endpoint controller to pass `tags` to the storage layer.

---

## Feature 2: Search & Combined Filters

### US-SF1: Text Search Across Title and Description
* **As a** board user,
* **I want to** search tasks using a text input bar,
* **So that** I can locate specific tasks by keywords in their title or description.

* **Acceptance Criteria:**
  1. `GET /tasks?search=keyword` performs a case-insensitive substring search on both task `title` and `description`.
  2. Matching tasks are returned in the response array with HTTP 200.
  3. If no matching tasks are found, an empty array `[]` is returned with HTTP 200.

* **AI Assumption Corrected:** The AI attempted to import an external search indexing library. I corrected this to use native Python substring matching (`search_lower in title.lower()`) on the in-memory array.

---

### US-SF2: Live Tag Filtering
* **As a** board user,
* **I want to** filter tasks by tag name,
* **So that** I can isolate tasks belonging to a specific category.

* **Acceptance Criteria:**
  1. `GET /tasks?tag=name` performs a case-insensitive match against any string inside each task's `tags` array.
  2. The frontend filter bar includes an input field that queries the backend as the user types.

* **AI Assumption Corrected:** The AI generated a frontend-only array filtering method that bypassed the API. I corrected it so the frontend passes `?tag=` to the backend, maintaining the backend as the single source of truth.

---

### US-SF3: Combined Multi-Constraint Querying
* **As a** board user,
* **I want to** combine text search, tag filter, and priority selection simultaneously,
* **So that** I can narrow down large task boards with precision.

* **Acceptance Criteria:**
  1. `GET /tasks` accepts combinations of `status`, `priority`, `search`, and `tag` parameters simultaneously.
  2. Sequential filtering logic applies all constraints cumulatively.
  3. The frontend implements input debouncing (300ms) on text fields to limit API request volume during typing.