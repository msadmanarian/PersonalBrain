from typing import Dict, List, Any
from personal_brain.core.tasks import TaskItem, TaskState

def evaluate_okr_alignment(objective_title: str, key_results_tasks: List[TaskItem]) -> Dict[str, Any]:
    total_hours = sum(t.estimated_hours for t in key_results_tasks)
    done_hours = sum(t.estimated_hours for t in key_results_tasks if t.state == TaskState.DONE)
    pct = round((done_hours / total_hours) * 100, 1) if total_hours > 0 else 0.0
    return {
        "objective": objective_title,
        "total_estimated_hours": total_hours,
        "completed_hours": done_hours,
        "completion_rate": pct,
    }
