from typing import Dict, Set, List

def find_connected_components(nodes: Set[str], adjacency: Dict[str, Set[str]]) -> List[Set[str]]:
    """Partition knowledge graph into disjoint clusters of interconnected concepts."""
    # Build undirected adjacency
    undirected = {n: set() for n in nodes}
    for src, targets in adjacency.items():
        for tgt in targets:
            if src in undirected and tgt in undirected:
                undirected[src].add(tgt)
                undirected[tgt].add(src)
    visited = set()
    clusters = []
    for node in nodes:
        if node not in visited:
            cluster = set()
            stack = [node]
            visited.add(node)
            while stack:
                curr = stack.pop()
                cluster.add(curr)
                for neighbor in undirected.get(curr, set()):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            clusters.append(cluster)
    return clusters
