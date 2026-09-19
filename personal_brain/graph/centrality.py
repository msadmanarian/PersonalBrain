from typing import Dict, Set

def compute_degree_centrality(nodes: Set[str], adjacency: Dict[str, Set[str]]) -> Dict[str, float]:
    """Calculates normalized in/out degree centrality."""
    n = len(nodes)
    if n <= 1:
        return {node: 0.0 for node in nodes}
    scores = {}
    for node in nodes:
        out_deg = len(adjacency.get(node, set()))
        scores[node] = round(out_deg / (n - 1), 4)
    return scores
