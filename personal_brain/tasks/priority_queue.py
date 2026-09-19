from typing import List
from personal_brain.core.tasks import TaskItem, TaskState

def get_actionable_tasks(tasks: List[TaskItem]) -> List[TaskItem]:
    """Return ready tasks sorted by highest priority."""
    actionable = [t for t in tasks if t.state in (TaskState.NEXT, TaskState.IN_PROGRESS)]
    actionable.sort(key=lambda t: t.priority.value, reverse=True)
    return actionable
