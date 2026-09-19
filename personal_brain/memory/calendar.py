import datetime
from typing import List, Dict
from personal_brain.core.review import ReviewCard

def generate_review_forecast(cards: List[ReviewCard], days_ahead: int = 7) -> Dict[str, int]:
    """Forecast expected daily review workload over the next N days."""
    today = datetime.date.today()
    forecast = {str(today + datetime.timedelta(days=i)): 0 for i in range(days_ahead)}
    for c in cards:
        due_date = datetime.date.fromtimestamp(c.next_review_at)
        due_str = str(due_date)
        if due_str in forecast:
            forecast[due_str] += 1
    return forecast
