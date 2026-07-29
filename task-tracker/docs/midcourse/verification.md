# Verification Evidence

## Baseline System Verification

======================================================================== test session starts ========================================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\ghadi\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker
plugins: anyio-4.12.1, cov-7.1.0
collected 32 items                                                                                                                                                     

tests/test_tasks.py::test_create_task_valid PASSED                                                                                                               [  3%]
tests/test_tasks.py::test_create_task_with_all_fields PASSED                                                                                                     [  6%]
tests/test_tasks.py::test_create_task_empty_title_rejected PASSED                                                                                                [  9%]
tests/test_tasks.py::test_create_task_whitespace_title_rejected PASSED                                                                                           [ 12%]
tests/test_tasks.py::test_create_task_title_over_200_chars_rejected PASSED                                                                                       [ 15%]
tests/test_tasks.py::test_create_task_extra_field_rejected PASSED                                                                                                [ 18%]
tests/test_tasks.py::test_list_tasks_empty PASSED                                                                                                                [ 21%]
tests/test_tasks.py::test_list_tasks_multiple PASSED                                                                                                             [ 25%]
tests/test_tasks.py::test_list_tasks_filter_by_priority PASSED                                                                                                   [ 28%]
tests/test_tasks.py::test_list_tasks_filter_by_status PASSED                                                                                                     [ 31%]
tests/test_tasks.py::test_get_task_by_id_found PASSED                                                                                                            [ 34%]
tests/test_tasks.py::test_get_task_by_id_not_found PASSED                                                                                                        [ 37%]
tests/test_tasks.py::test_update_task_title PASSED                                                                                                               [ 40%]
tests/test_tasks.py::test_update_task_multiple_fields PASSED                                                                                                     [ 43%]
tests/test_tasks.py::test_update_task_not_found PASSED                                                                                                           [ 46%]
tests/test_tasks.py::test_update_task_invalid_title PASSED                                                                                                       [ 50%]
tests/test_tasks.py::test_patch_unsupported_status_error PASSED                                                                                                  [ 53%]
tests/test_tasks.py::test_patch_invalid_priority_error PASSED                                                                                                    [ 56%]
tests/test_tasks.py::test_patch_non_existent_id PASSED                                                                                                           [ 59%]
tests/test_tasks.py::test_patch_extra_fields_rejected PASSED                                                                                                     [ 62%]
tests/test_tasks.py::test_transition_todo_to_inprogress_valid PASSED                                                                                             [ 65%]
tests/test_tasks.py::test_transition_inprogress_to_done_valid PASSED                                                                                             [ 68%]
tests/test_tasks.py::test_transition_done_to_inprogress_valid PASSED                                                                                             [ 71%]
tests/test_tasks.py::test_transition_todo_to_done_invalid PASSED                                                                                                 [ 75%]
tests/test_tasks.py::test_transition_inprogress_to_todo_invalid PASSED                                                                                           [ 78%]
tests/test_tasks.py::test_transition_done_to_todo_invalid PASSED                                                                                                 [ 81%]
tests/test_tasks.py::test_transition_same_to_same_invalid PASSED                                                                                                 [ 84%]
tests/test_tasks.py::test_delete_task_success PASSED                                                                                                             [ 87%]
tests/test_tasks.py::test_delete_task_not_found PASSED                                                                                                           [ 90%]
tests/test_tasks.py::test_delete_task_removes_from_list PASSED                                                                                                   [ 93%]
tests/test_tasks.py::test_health_endpoint PASSED                                                                                                                 [ 96%]
tests/test_tasks.py::test_root_endpoint PASSED                                                                                                                   [100%]

======================================================================= warnings summary =======================================================================
tests/test_tasks.py: 27 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:55: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow().isoformat()

tests/test_tasks.py: 41 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:40: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "last_updated": datetime.utcnow().isoformat()

tests/test_tasks.py: 10 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:152: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================ 32 passed, 78 warnings in 0.31s ================================================================

* **Initial Server Check:** `GET /health` returned HTTP 200 `{"status": "ok"}`.

## Final Backend Test Results
Ran full automated test suite after completing Features 1 and 2:


plugins: anyio-4.12.1, cov-7.1.0
collected 36 items                                                                                                                                               

tests/test_tasks.py::test_create_task_valid PASSED                                                                                                         [  2%]
tests/test_tasks.py::test_create_task_with_all_fields PASSED                                                                                               [  5%]
tests/test_tasks.py::test_create_task_empty_title_rejected PASSED                                                                                          [  8%]
tests/test_tasks.py::test_create_task_whitespace_title_rejected PASSED                                                                                     [ 11%]
tests/test_tasks.py::test_create_task_title_over_200_chars_rejected PASSED                                                                                 [ 13%]
tests/test_tasks.py::test_create_task_extra_field_rejected PASSED                                                                                          [ 16%]
tests/test_tasks.py::test_list_tasks_empty PASSED                                                                                                          [ 19%]
tests/test_tasks.py::test_list_tasks_multiple PASSED                                                                                                       [ 22%]
tests/test_tasks.py::test_list_tasks_filter_by_priority PASSED                                                                                             [ 25%]
tests/test_tasks.py::test_list_tasks_filter_by_status PASSED                                                                                               [ 27%]
tests/test_tasks.py::test_get_task_by_id_found PASSED                                                                                                      [ 30%]
tests/test_tasks.py::test_get_task_by_id_not_found PASSED                                                                                                  [ 33%]
tests/test_tasks.py::test_update_task_title PASSED                                                                                                         [ 36%]
tests/test_tasks.py::test_update_task_multiple_fields PASSED                                                                                               [ 38%]
tests/test_tasks.py::test_update_task_not_found PASSED                                                                                                     [ 41%]
tests/test_tasks.py::test_update_task_invalid_title PASSED                                                                                                 [ 44%]
tests/test_tasks.py::test_patch_unsupported_status_error PASSED                                                                                            [ 47%]
tests/test_tasks.py::test_patch_invalid_priority_error PASSED                                                                                              [ 50%]
tests/test_tasks.py::test_patch_non_existent_id PASSED                                                                                                     [ 52%]
tests/test_tasks.py::test_patch_extra_fields_rejected PASSED                                                                                               [ 55%]
tests/test_tasks.py::test_transition_todo_to_inprogress_valid PASSED                                                                                       [ 58%]
tests/test_tasks.py::test_transition_inprogress_to_done_valid PASSED                                                                                       [ 61%]
tests/test_tasks.py::test_transition_done_to_inprogress_valid PASSED                                                                                       [ 63%]
tests/test_tasks.py::test_transition_todo_to_done_invalid PASSED                                                                                           [ 66%]
tests/test_tasks.py::test_transition_inprogress_to_todo_invalid PASSED                                                                                     [ 69%]
tests/test_tasks.py::test_transition_done_to_todo_invalid PASSED                                                                                           [ 72%]
tests/test_tasks.py::test_transition_same_to_same_invalid PASSED                                                                                           [ 75%]
tests/test_tasks.py::test_delete_task_success PASSED                                                                                                       [ 77%]
tests/test_tasks.py::test_delete_task_not_found PASSED                                                                                                     [ 80%]
tests/test_tasks.py::test_delete_task_removes_from_list PASSED                                                                                             [ 83%]
tests/test_tasks.py::test_health_endpoint PASSED                                                                                                           [ 86%]
tests/test_tasks.py::test_root_endpoint PASSED                                                                                                             [ 88%]
tests/test_tasks.py::test_create_task_with_valid_tags PASSED                                                                                               [ 91%]
tests/test_tasks.py::test_create_task_invalid_tags_rejected PASSED                                                                                         [ 94%]
tests/test_tasks.py::test_filter_tasks_by_text_search PASSED                                                                                               [ 97%]
tests/test_tasks.py::test_filter_tasks_combined_query PASSED                                                                                               [100%]

======================================================================= warnings summary ========================================================================
tests/test_tasks.py: 33 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:55: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow().isoformat()

tests/test_tasks.py: 47 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:40: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "last_updated": datetime.utcnow().isoformat()

tests/test_tasks.py: 10 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:152: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_update_task_title
tests/test_tasks.py::test_update_task_multiple_fields
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:136: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================ 36 passed, 92 warnings in 0.39s ================================================================


## Manual browser checks: 
To verify browser interactions, start the application via uvicorn app.main:app --reload and open at http://localhost:5500

## Break Test evidence:

# 1
# Temporarily broken line in app/models/task.py
    if len(sanitized) > 10:  # Broken: allows up to 10 tags
        raise ValueError("cannot have more than 5 tags")

============================================================== test session starts ===============================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\ghadi\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker
plugins: anyio-4.12.1, cov-7.1.0
collected 36 items                                                                                                                                

tests/test_tasks.py::test_create_task_valid PASSED                                                                                          [  2%]
tests/test_tasks.py::test_create_task_with_all_fields PASSED                                                                                [  5%]
tests/test_tasks.py::test_create_task_empty_title_rejected PASSED                                                                           [  8%]
tests/test_tasks.py::test_create_task_whitespace_title_rejected PASSED                                                                      [ 11%]
tests/test_tasks.py::test_create_task_title_over_200_chars_rejected PASSED                                                                  [ 13%]
tests/test_tasks.py::test_create_task_extra_field_rejected PASSED                                                                           [ 16%]
tests/test_tasks.py::test_list_tasks_empty PASSED                                                                                           [ 19%]
tests/test_tasks.py::test_list_tasks_multiple PASSED                                                                                        [ 22%]
tests/test_tasks.py::test_list_tasks_filter_by_priority PASSED                                                                              [ 25%]
tests/test_tasks.py::test_list_tasks_filter_by_status PASSED                                                                                [ 27%]
tests/test_tasks.py::test_get_task_by_id_found PASSED                                                                                       [ 30%]
tests/test_tasks.py::test_get_task_by_id_not_found PASSED                                                                                   [ 33%]
tests/test_tasks.py::test_update_task_title PASSED                                                                                          [ 36%]
tests/test_tasks.py::test_update_task_multiple_fields PASSED                                                                                [ 38%]
tests/test_tasks.py::test_update_task_not_found PASSED                                                                                      [ 41%]
tests/test_tasks.py::test_update_task_invalid_title PASSED                                                                                  [ 44%]
tests/test_tasks.py::test_patch_unsupported_status_error PASSED                                                                             [ 47%]
tests/test_tasks.py::test_patch_invalid_priority_error PASSED                                                                               [ 50%]
tests/test_tasks.py::test_patch_non_existent_id PASSED                                                                                      [ 52%]
tests/test_tasks.py::test_patch_extra_fields_rejected PASSED                                                                                [ 55%]
tests/test_tasks.py::test_transition_todo_to_inprogress_valid PASSED                                                                        [ 58%]
tests/test_tasks.py::test_transition_inprogress_to_done_valid PASSED                                                                        [ 61%]
tests/test_tasks.py::test_transition_done_to_inprogress_valid PASSED                                                                        [ 63%]
tests/test_tasks.py::test_transition_todo_to_done_invalid PASSED                                                                            [ 66%]
tests/test_tasks.py::test_transition_inprogress_to_todo_invalid PASSED                                                                      [ 69%]
tests/test_tasks.py::test_transition_done_to_todo_invalid PASSED                                                                            [ 72%]
tests/test_tasks.py::test_transition_same_to_same_invalid PASSED                                                                            [ 75%]
tests/test_tasks.py::test_delete_task_success PASSED                                                                                        [ 77%]
tests/test_tasks.py::test_delete_task_not_found PASSED                                                                                      [ 80%]
tests/test_tasks.py::test_delete_task_removes_from_list PASSED                                                                              [ 83%]
tests/test_tasks.py::test_health_endpoint PASSED                                                                                            [ 86%]
tests/test_tasks.py::test_root_endpoint PASSED                                                                                              [ 88%]
tests/test_tasks.py::test_create_task_with_valid_tags PASSED                                                                                [ 91%]
tests/test_tasks.py::test_create_task_invalid_tags_rejected FAILED                                                                          [ 94%]
tests/test_tasks.py::test_filter_tasks_by_text_search PASSED                                                                                [ 97%]
tests/test_tasks.py::test_filter_tasks_combined_query PASSED                                                                                [100%]

==================================================================== FAILURES ====================================================================
_____________________________________________________ test_create_task_invalid_tags_rejected _____________________________________________________

client = <starlette.testclient.TestClient object at 0x000001A44C7AF200>

    def test_create_task_invalid_tags_rejected(client):
        """POST /tasks rejects more than 5 tags or tags longer than 20 characters."""
        # Test length validation
        response_long = client.post("/tasks", json={
            "title": "Task A",
            "tags": ["a" * 21]
        })
        assert response_long.status_code == 422
    
        # Test count validation
        response_count = client.post("/tasks", json={
            "title": "Task B",
            "tags": ["1", "2", "3", "4", "5", "6"]
        })
>       assert response_count.status_code == 422
E       assert 201 == 422
E        +  where 201 = <Response [201 Created]>.status_code

tests\test_tasks.py:393: AssertionError
================================================================ warnings summary ================================================================
tests/test_tasks.py: 34 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:55: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow().isoformat()

tests/test_tasks.py: 48 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:40: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "last_updated": datetime.utcnow().isoformat()

tests/test_tasks.py: 10 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:152: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_update_task_title
tests/test_tasks.py::test_update_task_multiple_fields
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:136: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_health_endpoint
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\main.py:58: DeprecationWarning: datetime.datetime.utcnow() is deprecatedand scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "timestamp": datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================ short test summary info =============================================================
FAILED tests/test_tasks.py::test_create_task_invalid_tags_rejected - assert 201 == 422
=================================================== 1 failed, 35 passed, 95 warnings in 0.55s ====================================================

# after revert

============================================================== test session starts ===============================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\ghadi\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker
plugins: anyio-4.12.1, cov-7.1.0
collected 36 items                                                                                                                                

tests/test_tasks.py::test_create_task_valid PASSED                                                                                          [  2%]
tests/test_tasks.py::test_create_task_with_all_fields PASSED                                                                                [  5%]
tests/test_tasks.py::test_create_task_empty_title_rejected PASSED                                                                           [  8%]
tests/test_tasks.py::test_create_task_whitespace_title_rejected PASSED                                                                      [ 11%]
tests/test_tasks.py::test_create_task_title_over_200_chars_rejected PASSED                                                                  [ 13%]
tests/test_tasks.py::test_create_task_extra_field_rejected PASSED                                                                           [ 16%]
tests/test_tasks.py::test_list_tasks_empty PASSED                                                                                           [ 19%]
tests/test_tasks.py::test_list_tasks_multiple PASSED                                                                                        [ 22%]
tests/test_tasks.py::test_list_tasks_filter_by_priority PASSED                                                                              [ 25%]
tests/test_tasks.py::test_list_tasks_filter_by_status PASSED                                                                                [ 27%]
tests/test_tasks.py::test_get_task_by_id_found PASSED                                                                                       [ 30%]
tests/test_tasks.py::test_get_task_by_id_not_found PASSED                                                                                   [ 33%]
tests/test_tasks.py::test_update_task_title PASSED                                                                                          [ 36%]
tests/test_tasks.py::test_update_task_multiple_fields PASSED                                                                                [ 38%]
tests/test_tasks.py::test_update_task_not_found PASSED                                                                                      [ 41%]
tests/test_tasks.py::test_update_task_invalid_title PASSED                                                                                  [ 44%]
tests/test_tasks.py::test_patch_unsupported_status_error PASSED                                                                             [ 47%]
tests/test_tasks.py::test_patch_invalid_priority_error PASSED                                                                               [ 50%]
tests/test_tasks.py::test_patch_non_existent_id PASSED                                                                                      [ 52%]
tests/test_tasks.py::test_patch_extra_fields_rejected PASSED                                                                                [ 55%]
tests/test_tasks.py::test_transition_todo_to_inprogress_valid PASSED                                                                        [ 58%]
tests/test_tasks.py::test_transition_inprogress_to_done_valid PASSED                                                                        [ 61%]
tests/test_tasks.py::test_transition_done_to_inprogress_valid PASSED                                                                        [ 63%]
tests/test_tasks.py::test_transition_todo_to_done_invalid PASSED                                                                            [ 66%]
tests/test_tasks.py::test_transition_inprogress_to_todo_invalid PASSED                                                                      [ 69%]
tests/test_tasks.py::test_transition_done_to_todo_invalid PASSED                                                                            [ 72%]
tests/test_tasks.py::test_transition_same_to_same_invalid PASSED                                                                            [ 75%]
tests/test_tasks.py::test_delete_task_success PASSED                                                                                        [ 77%]
tests/test_tasks.py::test_delete_task_not_found PASSED                                                                                      [ 80%]
tests/test_tasks.py::test_delete_task_removes_from_list PASSED                                                                              [ 83%]
tests/test_tasks.py::test_health_endpoint PASSED                                                                                            [ 86%]
tests/test_tasks.py::test_root_endpoint PASSED                                                                                              [ 88%]
tests/test_tasks.py::test_create_task_with_valid_tags PASSED                                                                                [ 91%]
tests/test_tasks.py::test_create_task_invalid_tags_rejected PASSED                                                                          [ 94%]
tests/test_tasks.py::test_filter_tasks_by_text_search PASSED                                                                                [ 97%]
tests/test_tasks.py::test_filter_tasks_combined_query PASSED                                                                                [100%]

================================================================ warnings summary ================================================================
tests/test_tasks.py: 33 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:55: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow().isoformat()

tests/test_tasks.py: 47 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:40: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "last_updated": datetime.utcnow().isoformat()

tests/test_tasks.py: 10 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:152: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_update_task_title
tests/test_tasks.py::test_update_task_multiple_fields
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:136: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_health_endpoint
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\main.py:58: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "timestamp": datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================== 36 passed, 93 warnings in 0.39s =========================================================


# 2
# Temporarily commented out in app/main.py
  # if search:
  #     search_lower = search.lower()
  #     tasks = [
  #         t for t in tasks 
  #         if (t.get("title") and search_lower in t["title"].lower()) or 
  #            (t.get("description") and search_lower in t["description"].lower())
  #     ]

============================================================== test session starts ===============================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\ghadi\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker
plugins: anyio-4.12.1, cov-7.1.0
collected 36 items                                                                                                                                

tests/test_tasks.py::test_create_task_valid PASSED                                                                                          [  2%]
tests/test_tasks.py::test_create_task_with_all_fields PASSED                                                                                [  5%]
tests/test_tasks.py::test_create_task_empty_title_rejected PASSED                                                                           [  8%]
tests/test_tasks.py::test_create_task_whitespace_title_rejected PASSED                                                                      [ 11%]
tests/test_tasks.py::test_create_task_title_over_200_chars_rejected PASSED                                                                  [ 13%]
tests/test_tasks.py::test_create_task_extra_field_rejected PASSED                                                                           [ 16%]
tests/test_tasks.py::test_list_tasks_empty PASSED                                                                                           [ 19%]
tests/test_tasks.py::test_list_tasks_multiple PASSED                                                                                        [ 22%]
tests/test_tasks.py::test_list_tasks_filter_by_priority PASSED                                                                              [ 25%]
tests/test_tasks.py::test_list_tasks_filter_by_status PASSED                                                                                [ 27%]
tests/test_tasks.py::test_get_task_by_id_found PASSED                                                                                       [ 30%]
tests/test_tasks.py::test_get_task_by_id_not_found PASSED                                                                                   [ 33%]
tests/test_tasks.py::test_update_task_title PASSED                                                                                          [ 36%]
tests/test_tasks.py::test_update_task_multiple_fields PASSED                                                                                [ 38%]
tests/test_tasks.py::test_update_task_not_found PASSED                                                                                      [ 41%]
tests/test_tasks.py::test_update_task_invalid_title PASSED                                                                                  [ 44%]
tests/test_tasks.py::test_patch_unsupported_status_error PASSED                                                                             [ 47%]
tests/test_tasks.py::test_patch_invalid_priority_error PASSED                                                                               [ 50%]
tests/test_tasks.py::test_patch_non_existent_id PASSED                                                                                      [ 52%]
tests/test_tasks.py::test_patch_extra_fields_rejected PASSED                                                                                [ 55%]
tests/test_tasks.py::test_transition_todo_to_inprogress_valid PASSED                                                                        [ 58%]
tests/test_tasks.py::test_transition_inprogress_to_done_valid PASSED                                                                        [ 61%]
tests/test_tasks.py::test_transition_done_to_inprogress_valid PASSED                                                                        [ 63%]
tests/test_tasks.py::test_transition_todo_to_done_invalid PASSED                                                                            [ 66%]
tests/test_tasks.py::test_transition_inprogress_to_todo_invalid PASSED                                                                      [ 69%]
tests/test_tasks.py::test_transition_done_to_todo_invalid PASSED                                                                            [ 72%]
tests/test_tasks.py::test_transition_same_to_same_invalid PASSED                                                                            [ 75%]
tests/test_tasks.py::test_delete_task_success PASSED                                                                                        [ 77%]
tests/test_tasks.py::test_delete_task_not_found PASSED                                                                                      [ 80%]
tests/test_tasks.py::test_delete_task_removes_from_list PASSED                                                                              [ 83%]
tests/test_tasks.py::test_health_endpoint PASSED                                                                                            [ 86%]
tests/test_tasks.py::test_root_endpoint PASSED                                                                                              [ 88%]
tests/test_tasks.py::test_create_task_with_valid_tags PASSED                                                                                [ 91%]
tests/test_tasks.py::test_create_task_invalid_tags_rejected PASSED                                                                          [ 94%]
tests/test_tasks.py::test_filter_tasks_by_text_search FAILED                                                                                [ 97%]
tests/test_tasks.py::test_filter_tasks_combined_query PASSED                                                                                [100%]

==================================================================== FAILURES ====================================================================
________________________________________________________ test_filter_tasks_by_text_search ________________________________________________________

client = <starlette.testclient.TestClient object at 0x000001D7FDA37440>

    def test_filter_tasks_by_text_search(client):
        """GET /tasks?search=deploy filters tasks by title and description case-insensitively."""
        client.post("/tasks", json={"title": "Deploy production app", "description": "urgent stuff"})
        client.post("/tasks", json={"title": "Write documentation", "description": "Need to deploy to docs site"})
        client.post("/tasks", json={"title": "Buy groceries"})
    
        # Case-insensitive title match
        r1 = client.get("/tasks?search=DEPLOY")
        assert r1.status_code == 200
>       assert len(r1.json()) == 2
E       AssertionError: assert 3 == 2
E        +  where 3 = len([{'assignee': None, 'created_at': '2026-07-26T16:38:35.498643', 'description': 'urgent stuff', 'id': 1, ...}, {'assignee': None, 'created_at': '2026-07-26T16:38:35.502389', 'description': 'Need to deploy to docs site', 'id': 2, ...}, {'assignee': None, 'created_at': '2026-07-26T16:38:35.506392', 'description': ' ', 'id': 3, ...}])
E        +    where [{'assignee': None, 'created_at': '2026-07-26T16:38:35.498643', 'description': 'urgent stuff', 'id': 1, ...}, {'assignee': None, 'created_at': '2026-07-26T16:38:35.502389', 'description': 'Need to deploy to docs site', 'id': 2, ...}, {'assignee': None, 'created_at': '2026-07-26T16:38:35.506392', 'description': ' ', 'id': 3, ...}] = json()
E        +      where json = <Response [200 OK]>.json

tests\test_tasks.py:405: AssertionError
================================================================ warnings summary ================================================================
tests/test_tasks.py: 33 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:55: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow().isoformat()

tests/test_tasks.py: 47 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:40: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "last_updated": datetime.utcnow().isoformat()

tests/test_tasks.py: 10 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:152: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_update_task_title
tests/test_tasks.py::test_update_task_multiple_fields
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:136: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_health_endpoint
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\main.py:58: DeprecationWarning: datetime.datetime.utcnow() is deprecatedand scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "timestamp": datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================ short test summary info =============================================================
FAILED tests/test_tasks.py::test_filter_tasks_by_text_search - AssertionError: assert 3 == 2
=================================================== 1 failed, 35 passed, 93 warnings in 0.54s ====================================================

# after revert

============================================================== test session starts ===============================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\ghadi\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker
plugins: anyio-4.12.1, cov-7.1.0
collected 36 items                                                                                                                                

tests/test_tasks.py::test_create_task_valid PASSED                                                                                          [  2%]
tests/test_tasks.py::test_create_task_with_all_fields PASSED                                                                                [  5%]
tests/test_tasks.py::test_create_task_empty_title_rejected PASSED                                                                           [  8%]
tests/test_tasks.py::test_create_task_whitespace_title_rejected PASSED                                                                      [ 11%]
tests/test_tasks.py::test_create_task_title_over_200_chars_rejected PASSED                                                                  [ 13%]
tests/test_tasks.py::test_create_task_extra_field_rejected PASSED                                                                           [ 16%]
tests/test_tasks.py::test_list_tasks_empty PASSED                                                                                           [ 19%]
tests/test_tasks.py::test_list_tasks_multiple PASSED                                                                                        [ 22%]
tests/test_tasks.py::test_list_tasks_filter_by_priority PASSED                                                                              [ 25%]
tests/test_tasks.py::test_list_tasks_filter_by_status PASSED                                                                                [ 27%]
tests/test_tasks.py::test_get_task_by_id_found PASSED                                                                                       [ 30%]
tests/test_tasks.py::test_get_task_by_id_not_found PASSED                                                                                   [ 33%]
tests/test_tasks.py::test_update_task_title PASSED                                                                                          [ 36%]
tests/test_tasks.py::test_update_task_multiple_fields PASSED                                                                                [ 38%]
tests/test_tasks.py::test_update_task_not_found PASSED                                                                                      [ 41%]
tests/test_tasks.py::test_update_task_invalid_title PASSED                                                                                  [ 44%]
tests/test_tasks.py::test_patch_unsupported_status_error PASSED                                                                             [ 47%]
tests/test_tasks.py::test_patch_invalid_priority_error PASSED                                                                               [ 50%]
tests/test_tasks.py::test_patch_non_existent_id PASSED                                                                                      [ 52%]
tests/test_tasks.py::test_patch_extra_fields_rejected PASSED                                                                                [ 55%]
tests/test_tasks.py::test_transition_todo_to_inprogress_valid PASSED                                                                        [ 58%]
tests/test_tasks.py::test_transition_inprogress_to_done_valid PASSED                                                                        [ 61%]
tests/test_tasks.py::test_transition_done_to_inprogress_valid PASSED                                                                        [ 63%]
tests/test_tasks.py::test_transition_todo_to_done_invalid PASSED                                                                            [ 66%]
tests/test_tasks.py::test_transition_inprogress_to_todo_invalid PASSED                                                                      [ 69%]
tests/test_tasks.py::test_transition_done_to_todo_invalid PASSED                                                                            [ 72%]
tests/test_tasks.py::test_transition_same_to_same_invalid PASSED                                                                            [ 75%]
tests/test_tasks.py::test_delete_task_success PASSED                                                                                        [ 77%]
tests/test_tasks.py::test_delete_task_not_found PASSED                                                                                      [ 80%]
tests/test_tasks.py::test_delete_task_removes_from_list PASSED                                                                              [ 83%]
tests/test_tasks.py::test_health_endpoint PASSED                                                                                            [ 86%]
tests/test_tasks.py::test_root_endpoint PASSED                                                                                              [ 88%]
tests/test_tasks.py::test_create_task_with_valid_tags PASSED                                                                                [ 91%]
tests/test_tasks.py::test_create_task_invalid_tags_rejected PASSED                                                                          [ 94%]
tests/test_tasks.py::test_filter_tasks_by_text_search PASSED                                                                                [ 97%]
tests/test_tasks.py::test_filter_tasks_combined_query PASSED                                                                                [100%]

================================================================ warnings summary ================================================================
tests/test_tasks.py: 33 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:55: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow().isoformat()

tests/test_tasks.py: 47 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:40: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "last_updated": datetime.utcnow().isoformat()

tests/test_tasks.py: 10 warnings
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:152: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_update_task_title
tests/test_tasks.py::test_update_task_multiple_fields
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\storage\tasks.py:136: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    task["updated_at"] = datetime.utcnow().isoformat()

tests/test_tasks.py::test_health_endpoint
  C:\Users\ghadi\OneDrive\Desktop\AUB\AI-Assisted-Coding\task-tracker\app\main.py:58: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    "timestamp": datetime.utcnow().isoformat()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================== 36 passed, 93 warnings in 0.36s =========================================================