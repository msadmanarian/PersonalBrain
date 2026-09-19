from personal_brain.memory.scheduler import get_due_cards
from personal_brain.memory.recorder import record_card_review

def run_terminal_review(cards: list):
    due = get_due_cards(cards)
    print(f"[+] {len(due)} cards due for spaced review.")
    return due
