from typing import Dict, Set

def compute_pagerank(
    nodes: Set[str],
    adjacency: Dict[str, Set[str]],
    damping: float = 0.85,
    max_iter: int = 50,
    tol: float = 1e-5
) -> Dict[str, float]:
    """Compute PageRank centrality scores for personal knowledge graph."""
    n = len(nodes)
    if n == 0:
        return {}
    ranks = {node: 1.0 / n for node in nodes}
    for _ in range(max_iter):
        new_ranks = {}
        dangling_sum = sum(ranks[node] for node in nodes if not adjacency.get(node))
        for node in nodes:
            rank_sum = 0.0
            for src, targets in adjacency.items():
                if node in targets:
                    rank_sum += ranks[src] / len(targets)
            new_rank = (1.0 - damping) / n + damping * (rank_sum + dangling_sum / n)
            new_ranks[node] = new_rank
        # Check convergence
        diff = sum(abs(new_ranks[node] - ranks[node]) for node in nodes)
        ranks = new_ranks
        if diff < tol:
            break
    return ranks
