from typing import Dict, List, Tuple
from personal_brain.tasks.dag import TaskDAG
from personal_brain.tasks.toposort import topological_sort

def calculate_critical_path(dag: TaskDAG) -> Tuple[List[str], float]:
    """Critical Path Method (CPM) identifying the longest dependent chain of tasks."""
    order = topological_sort(dag)
    if not order:
        return [], 0.0
    earliest_finish = {t_id: 0.0 for t_id in dag.tasks}
    predecessors = {t_id: None for t_id in dag.tasks}
    for t_id in order:
        task = dag.tasks[t_id]
        dur = task.estimated_hours
        dep_finish = max([earliest_finish[d] for d in task.dependencies], default=0.0)
        earliest_finish[t_id] = dep_finish + dur
        # Track longest path predecessor
        for d in task.dependencies:
            if earliest_finish[d] == dep_finish:
                predecessors[t_id] = d
                break
    # Find maximum finish task
    end_task = max(earliest_finish.keys(), key=lambda k: earliest_finish[k], default=None)
    if not end_task:
        return [], 0.0
    path = []
    curr = end_task
    while curr:
        path.insert(0, curr)
        curr = predecessors[curr]
    return path, earliest_finish[end_task]
