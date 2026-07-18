# Business Logic for Task Tracker
# Part 2.3: Status transition validation

from app.models import TaskStatus

# Valid status transitions as a frozenset of (from_status, to_status) tuples
VALID_TRANSITIONS = frozenset([
    (TaskStatus.TODO.value, TaskStatus.IN_PROGRESS.value),      # ToDo → InProgress ✓
    (TaskStatus.IN_PROGRESS.value, TaskStatus.DONE.value),      # InProgress → Done ✓
    (TaskStatus.DONE.value, TaskStatus.IN_PROGRESS.value),      # Done → InProgress ✓
])

# Invalid transitions:
# ToDo → Done ✗
# Done → ToDo ✗
# same → same ✗


def validate_status_transition(current_status: str, new_status: str) -> bool:
    """
    Validate a status transition.
    
    Args:
        current_status: Current task status (e.g., "ToDo")
        new_status: Desired new status (e.g., "InProgress")
    
    Returns:
        True if transition is valid, False otherwise
    
    Rules:
    - ToDo → InProgress: OK
    - InProgress → Done: OK
    - Done → InProgress: OK
    - ToDo → Done: NOT OK
    - Done → ToDo: NOT OK
    - same → same: NOT OK
    """
    # Reject same-to-same transitions
    if current_status == new_status:
        return False
    
    # Check if transition is in valid set
    return (current_status, new_status) in VALID_TRANSITIONS
