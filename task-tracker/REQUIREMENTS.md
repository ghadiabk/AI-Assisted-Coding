# Task Tracker - User Stories and Requirements

## Project Context
- **Stack:** Python, FastAPI
- **Scope:** CRUD operations for tasks with status and priority filtering
- **Task Fields:** id, title, description, status, priority, assignee
- **Out of scope:** Authentication, multi-tenancy, real-time updates, external database

---

## User Stories (AI-Generated + Reviewed)

### Story 1: Create a Task
**As a** team member  
**I want to** create a new task  
**So that** I can track work to be done

**Acceptance Criteria:**
- POST /tasks accepts title (required), description (optional), priority, assignee
- Title must be non-empty after stripping whitespace
- Returns 422 with error details if title is empty or invalid
- Returns 201 with created task object including auto-generated id
- Created task appears in the task list
- Default status is "ToDo" when created

**Review notes:** AI defaulted to accepting any input. Added validation constraint.

---

### Story 2: View All Tasks
**As a** team member  
**I want to** view all tasks  
**So that** I can see what work exists

**Acceptance Criteria:**
- GET /tasks returns a list of all tasks
- Returns 200 with array of task objects in predictable shape
- Empty list returns [] not null
- Each task includes id, title, description, status, priority, assignee

**Review notes:** AI included unnecessary filtering here. Kept it simple per scope.

---

### Story 3: Filter Tasks by Status
**As a** team member  
**I want to** filter tasks by status  
**So that** I can focus on specific workflow stages

**Acceptance Criteria:**
- GET /tasks?status=ToDo filters by status
- Valid statuses: "ToDo", "InProgress", "Done"
- Invalid status value returns 422 with error message
- Multiple statuses not supported in Module 1
- Returns empty list if no tasks match

**Review notes:** **AI ASSUMPTION REJECTED:** AI suggested allowing any arbitrary status string. Statuses must be a fixed enum.

---

### Story 4: Filter Tasks by Priority
**As a** team member  
**I want to** filter tasks by priority  
**So that** I can prioritize high-impact work

**Acceptance Criteria:**
- GET /tasks?priority=High filters by priority
- Valid priorities: "Low", "Medium", "High"
- Invalid priority value returns 422 with error message
- Returns empty list if no tasks match

**Review notes:** Same constraint as status. Must validate against enum.

---

### Story 5: Update Task Details
**As a** team member  
**I want to** update task details (title, description, priority, assignee)  
**So that** I can keep task information current

**Acceptance Criteria:**
- PATCH /tasks/:id accepts title, description, priority, assignee (all optional)
- Only provided fields are updated; omitted fields unchanged
- Returns 404 if task id does not exist
- Returns 422 if provided values are invalid (empty title, invalid priority/status)
- Returns 200 with updated task object

**Review notes:** AI wanted to allow updating status here. Separated status updates into a dedicated endpoint per business rules.

---

### Story 6: Update Task Status (Controlled Transitions)
**As a** team member  
**I want to** move a task through status stages  
**So that** I can reflect work progress

**Acceptance Criteria:**
- PATCH /tasks/:id/status accepts new_status in body
- Valid transitions: ToDo → InProgress, InProgress → Done
- **Done tasks cannot transition back** to InProgress or ToDo
- Invalid transitions return 400 with reason
- Returns 404 if task id does not exist
- Returns 200 with updated task object

**Review notes:** **AI ASSUMPTION REJECTED:** AI generated shallow status update that allowed any transition. Added business rules: Done is terminal until explicit reset requirement clarified.

---

### Story 7: Delete a Task
**As a** team member  
**I want to** delete a task  
**So that** I can remove completed or obsolete work

**Acceptance Criteria:**
- DELETE /tasks/:id removes task by id
- Returns 404 if task id does not exist
- Returns 204 (No Content) on success
- Deleted task no longer appears in task list

**Review notes:** AI forgot to specify status code for missing task. Added 404 requirement.

---

### Story 8: Validate Task Data
**As a** system  
**I want to** validate all task inputs  
**So that** invalid data does not corrupt the task list

**Acceptance Criteria:**
- Empty title (empty string "") is rejected
- Whitespace-only title ("   ") is rejected after trimming
- Title > 255 characters is rejected
- Invalid status values rejected
- Invalid priority values rejected
- Priority field is required; cannot be null
- Returns 422 with error message describing what failed

**Review notes:** **AI ASSUMPTION:** AI initially made description and priority optional. Clarified that priority is required; description truly optional.

---

## Summary of AI Corrections
1. ✅ Added enum validation for status and priority (not free-form strings)
2. ✅ Added whitespace trimming and validation for title
3. ✅ Separated status transitions into controlled business logic (Done is terminal)
4. ✅ Clarified that deleted tasks return 404, not 200
5. ✅ Made priority a required field
6. ✅ Specified 201 for create, 204 for delete success

---

## Next Step
Use these refined stories as context for the **Architecture Decision Record** (Part B).
