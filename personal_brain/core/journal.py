from dataclasses import dataclass, field
from typing import List, Dict, Any
import time

@dataclass
class JournalEntry:
    date_str: str # YYYY-MM-DD
    content: str
    mood_score: int = 5 # 1-10
    energy_level: int = 5 # 1-10
    tags: List[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)

@dataclass
class HabitStreak:
    habit_name: str
    current_streak: int = 0
    longest_streak: int = 0
    last_completed_date: str = ""
