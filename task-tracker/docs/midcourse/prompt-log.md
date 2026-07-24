# Prompt Log

## Feature 1: Tags & Labels

### Prompt 1.1: Pydantic Tag Validation (Weak vs. Strong Rewrite)
* **Weak Original Prompt:**  
  > "Add tags to tasks in my model file."
* **Strong Rewritten Prompt:**  
  > **Role:** Senior FastAPI Developer  
  > **Task:** Update `TaskCreate`, `TaskUpdate`, and `TaskResponse` in `app/models/task.py` to support task tags.  
  > **Constraints:** Represent tags as `Optional[List[str]]`. Use Pydantic v2 `@field_validator("tags", mode="before")`. Strip whitespace from each tag and ignore blank strings. Raise a `ValueError` if tag count > 5 or if any tag length > 20 chars. Do not alter title or priority validators.  
  > **Output Format:** Code block only.
* **AI Output:** The AI generated model structures using Pydantic v2 syntax.
* **Decision:** Accepted after verifying that `mode="before"` handled empty lists and non-trimmed string inputs properly.

### Prompt 1.2: Storage Layer Extension
* **Prompt:**  
  > **Role:** Python Engineer  
  > **Task:** Modify `add_task` and `update_task` in `app/storage/tasks.py` to handle the `tags` list parameter.  
  > **Constraints:** Default `tags` to `[]` when `None`. Preserve existing `json.dump` file persistence logic.  
  > **Output Format:** Modified storage functions only.
* **AI Output:** Updated `add_task` and `update_task` function signatures and internal dictionary assignments.
* **Decision:** Accepted and applied.

### Prompt 1.3: Frontend Modal Tag Input
* **Prompt:**  
  > Add a comma-separated tags input field to the HTML modal in `frontend/index.html`. Update `openCreateModal` to clear it, `openEditModal` to prefill it with `.join(', ')`, and render tag chips on each card.
* **AI Output:** Generated HTML markup, CSS styling for `.tag-chip`, and JavaScript DOM handling.
* **Decision:** Edited. The initial code omitted parsing the input back into an array on submission. I added `.split(',').map(t => t.trim()).filter(Boolean)` to fix the array conversion.

---

## Feature 2: Search & Combined Filters

### Prompt 2.1: Extended GET Endpoint (Weak vs. Strong Rewrite)
* **Weak Original Prompt:**  
  > "Make search work in main.py."
* **Strong Rewritten Prompt:**  
  > **Role:** Senior FastAPI Developer  
  > **Task:** Update `list_tasks` in `app/main.py` to support search and tag parameters.  
  > **Constraints:** Add optional query parameters `search` and `tag`. Perform case-insensitive substring search on title and description for `search`. Perform case-insensitive matching against the `tags` list for `tag`. Combine all active filters (`status`, `priority`, `search`, `tag`) sequentially on `get_all_tasks()`. Return HTTP 200 with `[]` if no matches occur.  
  > **Output Format:** `list_tasks` function block only.
* **AI Output:** Provided the updated `list_tasks` endpoint function with sequential list comprehension checks.
* **Decision:** Accepted without modification.

### Prompt 2.2: Live Filter UI and Debounce
* **Prompt:**  
  > Add a filter bar above the board in `frontend/index.html` with inputs for search, priority, and tag filter. Update `fetchTasks` to build dynamic `URLSearchParams` and add a 300ms debounce helper for text input events.
* **AI Output:** HTML filter bar markup, CSS layout styles, debounced event listeners, and updated `fetchTasks()` implementation.
* **Decision:** Accepted after testing in the browser to confirm live filtering worked without sending excess network requests.

### Prompt 2.3: Pytest Expansion
* **Prompt:**  
  > Generate pytest tests in `tests/test_tasks.py` to test tag creation sanitization, tag limit validation errors (422), text search filtering, and combined multi-parameter queries.
* **AI Output:** Four new test functions covering the specified scenarios.
* **Decision:** Accepted and added to the suite.