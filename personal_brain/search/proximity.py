from typing import Dict, List, Set

def get_concept_neighborhood(node_id: str, adjacency: Dict[str, Set[str]], depth: int = 2) -> Set[str]:
    visited = {node_id}
    current_layer = {node_id}
    for _ in range(depth):
        next_layer = set()
        for curr in current_layer:
            for neighbor in adjacency.get(curr, set()):
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_layer.add(neighbor)
        current_layer = next_layer
    return visited
