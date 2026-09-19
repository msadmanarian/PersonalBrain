from typing import List, Dict, Any
from personal_brain.core.review import ReviewCard

def compute_memory_stats(cards: List[ReviewCard]) -> Dict[str, Any]:
    total = len(cards)
    if total == 0:
        return {"total_cards": 0, "avg_ease": 2.5, "mature_cards": 0}
    mature = sum(1 for c in cards if c.interval_days >= 21)
    avg_ease = sum(c.ease_factor for c in cards) / total
    return {
        "total_cards": total,
        "mature_cards": mature,
        "young_cards": total - mature,
        "avg_ease": round(avg_ease, 2),
    }
