import time
from typing import List
from personal_brain.core.review import ReviewCard

def get_due_cards(cards: List[ReviewCard], current_time: float = None) -> List[ReviewCard]:
    """Filter cards due for active spaced repetition review."""
    now = current_time or time.time()
    due = [c for c in cards if c.next_review_at <= now]
    due.sort(key=lambda c: c.next_review_at)
    return due
