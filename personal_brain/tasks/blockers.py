from typing import List
from personal_brain.tasks.dag import TaskDAG
from personal_brain.core.tasks import TaskState

def find_blocked_tasks(dag: TaskDAG) -> List[str]:
    """Identify tasks waiting on incomplete dependencies."""
    blocked = []
    for t_id, task in dag.tasks.items():
        if task.state == TaskState.DONE:
            continue
        for dep in task.dependencies:
            dep_task = dag.tasks.get(dep)
            if dep_task and dep_task.state != TaskState.DONE:
                blocked.append(t_id)
                break
    return blocked
