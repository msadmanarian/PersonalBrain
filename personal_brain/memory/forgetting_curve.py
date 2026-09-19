import math
import time

def estimate_retention_probability(last_reviewed_at: float, interval_days: float, current_time: float = None) -> float:
    """Ebbinghaus exponential forgetting curve R = exp(-t / S)."""
    if not last_reviewed_at:
        return 0.1
    now = current_time or time.time()
    elapsed_days = max(0.0, (now - last_reviewed_at) / 86400.0)
    stability = max(0.5, interval_days)
    retention = math.exp(-elapsed_days / stability)
    return round(min(1.0, max(0.0, retention)), 3)
