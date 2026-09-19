from typing import Dict, Set, List, Optional
from collections import deque

def find_shortest_path(start_id: str, target_id: str, adjacency: Dict[str, Set[str]]) -> Optional[List[str]]:
    """BFS shortest path between two knowledge nodes."""
    if start_id == target_id:
        return [start_id]
    queue = deque([[start_id]])
    visited = {start_id}
    while queue:
        path = queue.popleft()
        curr = path[-1]
        for neighbor in adjacency.get(curr, set()):
            if neighbor == target_id:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None
