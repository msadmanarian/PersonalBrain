import time
from personal_brain.core.review import ReviewCard
from personal_brain.memory.sm2 import calculate_sm2

def record_card_review(card: ReviewCard, quality_grade: int) -> ReviewCard:
    """Apply SM-2 algorithm and update card review schedule."""
    reps, ef, interval = calculate_sm2(
        repetitions=card.repetitions,
        ease_factor=card.ease_factor,
        interval_days=card.interval_days,
        quality=quality_grade
    )
    card.repetitions = reps
    card.ease_factor = ef
    card.interval_days = interval
    now = time.time()
    card.last_reviewed_at = now
    card.next_review_at = now + (interval * 86400.0)
    if quality_grade < 3:
        card.leech_count += 1
    return card
