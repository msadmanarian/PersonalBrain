import re
from typing import List, Tuple
from personal_brain.core.review import ReviewCard

FLASHCARD_REGEX = re.compile(r"Q::\s*(.*?)\s*A::\s*(.*?)(?=\nQ::|\Z)", re.DOTALL)

def extract_flashcards_from_markdown(content: str, node_id: str) -> List[ReviewCard]:
    """Parse inline flashcard syntax (Q:: Question A:: Answer) from note markdown."""
    cards = []
    for match in FLASHCARD_REGEX.finditer(content):
        q = match.group(1).strip()
        a = match.group(2).strip()
        if q and a:
            cards.append(ReviewCard(question=q, answer=a, node_id=node_id))
    return cards
