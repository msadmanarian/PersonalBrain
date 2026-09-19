from typing import Dict, Set, List

def detect_cycles(nodes: Set[str], adjacency: Dict[str, Set[str]]) -> List[List[str]]:
    """Detect circular references and dependency loops in knowledge graph."""
    visited = {}
    cycles = []
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = {n: 0 for n in nodes}
    path = []
    def dfs(curr):
        state[curr] = 1
        path.append(curr)
        for neighbor in adjacency.get(curr, set()):
            if state.get(neighbor) == 1:
                cycle_start = path.index(neighbor)
                cycles.append(path[cycle_start:] + [neighbor])
            elif state.get(neighbor) == 0:
                dfs(neighbor)
        path.pop()
        state[curr] = 2
    for node in nodes:
        if state[node] == 0:
            dfs(node)
    return cycles
