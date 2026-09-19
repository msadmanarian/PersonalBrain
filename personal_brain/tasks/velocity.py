from typing import List
from personal_brain.core.tasks import TaskItem, TaskState
import time

def calculate_completion_velocity(tasks: List[TaskItem], window_days: float = 7.0) -> float:
    """Calculate tasks completed per day over the specified window."""
    now = time.time()
    cutoff = now - (window_days * 86400.0)
    done_count = sum(1 for t in tasks if t.state == TaskState.DONE and t.completed_at and t.completed_at >= cutoff)
    return round(done_count / window_days, 2)
