from typing import List
from personal_brain.core.tasks import TaskItem, TaskState, Priority
import time

def escalate_overdue_tasks(tasks: List[TaskItem]) -> int:
    """Escalate priority of overdue tasks to URGENT."""
    now = time.time()
    escalated = 0
    for t in tasks:
        if t.due_date and t.due_date < now and t.state != TaskState.DONE:
            if t.priority != Priority.URGENT:
                t.priority = Priority.URGENT
                escalated += 1
    return escalated
