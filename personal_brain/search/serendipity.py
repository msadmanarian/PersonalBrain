import random
from typing import List, Dict, Optional
from personal_brain.core.search_types import SerendipityMatch
from personal_brain.search.similarity import cosine_similarity

def find_serendipitous_connection(
    nodes: Dict[str, Dict[str, Any]],
    vectors: Dict[str, Dict[str, float]],
    adjacency: Dict[str, set]
) -> Optional[SerendipityMatch]:
    """Find two conceptual nodes that share semantic affinity but lack a direct link."""
    node_ids = list(nodes.keys())
    if len(node_ids) < 2:
        return None
    candidates = []
    # Sample pairs
    for _ in range(50):
        src, tgt = random.sample(node_ids, 2)
        # Check if already linked
        if tgt not in adjacency.get(src, set()) and src not in adjacency.get(tgt, set()):
            sim = cosine_similarity(vectors.get(src, {}), vectors.get(tgt, {}))
            if 0.25 <= sim <= 0.85: # Meaningful but not identical
                shared_terms = set(vectors.get(src, {}).keys()).intersection(vectors.get(tgt, {}).keys())
                bridge = ", ".join(list(shared_terms)[:3]) if shared_terms else "Associative bridge"
                candidates.append((src, tgt, sim, bridge))
    if not candidates:
        return None
    best = max(candidates, key=lambda x: x[2])
    return SerendipityMatch(
        source_node_id=best[0],
        source_title=nodes[best[0]]["title"],
        target_node_id=best[1],
        target_title=nodes[best[1]]["title"],
        associative_bridge=best[3],
        affinity_score=best[2],
    )
