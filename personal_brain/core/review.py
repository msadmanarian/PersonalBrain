from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import time
import uuid

@dataclass
class ReviewCard:
    question: str
    answer: str
    node_id: str
    card_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    repetitions: int = 0
    interval_days: float = 1.0
    ease_factor: float = 2.5
    next_review_at: float = field(default_factory=time.time)
    last_reviewed_at: Optional[float] = None
    leech_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "card_id": self.card_id,
            "node_id": self.node_id,
            "question": self.question,
            "answer": self.answer,
            "repetitions": self.repetitions,
            "interval_days": round(self.interval_days, 2),
            "ease_factor": round(self.ease_factor, 3),
            "next_review_at": self.next_review_at,
            "leech_count": self.leech_count,
        }
