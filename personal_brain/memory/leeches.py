from typing import List
from personal_brain.core.review import ReviewCard

def detect_leech_cards(cards: List[ReviewCard], threshold: int = 4) -> List[ReviewCard]:
    """Detect persistently failed flashcards that require note re-structuring."""
    return [c for c in cards if c.leech_count >= threshold]
