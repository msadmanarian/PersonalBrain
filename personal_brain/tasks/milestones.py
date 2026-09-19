from typing import List, Dict, Any
from personal_brain.core.tasks import TaskItem, TaskState

def compute_milestone_progress(tasks: List[TaskItem]) -> Dict[str, Any]:
    total = len(tasks)
    if total == 0:
        return {"total": 0, "completed": 0, "progress_percent": 100.0}
    done = sum(1 for t in tasks if t.state == TaskState.DONE)
    return {
        "total": total,
        "completed": done,
        "progress_percent": round((done / total) * 100, 1),
    }
