from typing import Dict

def cosine_similarity(vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
    """Calculates cosine similarity between two sparse vector representations."""
    dot_product = 0.0
    for term, val in vec1.items():
        if term in vec2:
            dot_product += val * vec2[term]
    return round(min(1.0, max(0.0, dot_product)), 4)
