from typing import List, Optional
from personal_brain.tasks.dag import TaskDAG

def topological_sort(dag: TaskDAG) -> Optional[List[str]]:
    """Kahn's algorithm for linear execution order of task dependencies."""
    in_degree = {t_id: len(dag.in_adj.get(t_id, set())) for t_id in dag.tasks}
    queue = [t_id for t_id, deg in in_degree.items() if deg == 0]
    result = []
    while queue:
        curr = queue.pop(0)
        result.append(curr)
        for neighbor in dag.adj.get(curr, set()):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(dag.tasks):
        return None # Circular dependency cycle detected
    return result
