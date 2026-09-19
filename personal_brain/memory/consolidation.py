from typing import List, Dict, Any
from personal_brain.core.review import ReviewCard
from personal_brain.memory.telemetry import compute_memory_stats

def generate_memory_consolidation_report(cards: List[ReviewCard]) -> Dict[str, Any]:
    stats = compute_memory_stats(cards)
    return {
        "status": "nominal" if stats["total_cards"] > 0 else "empty",
        "retention_index": round(stats.get("avg_ease", 2.5) / 2.5 * 100, 1),
        "metrics": stats,
    }
