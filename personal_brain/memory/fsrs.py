import math

def calculate_memory_stability(stability: float, difficulty: float, grade: int) -> float:
    """Modern FSRS memory stability evolution based on cognitive retrieval practice."""
    if grade >= 3:
        factor = 1.0 + math.exp(1.0 - difficulty / 5.0)
        return stability * factor
    return max(0.5, stability * 0.3)
