from typing import Dict, Any

def render_flashcard_component(card_data: Dict[str, Any]) -> str:
    return f"""
    <div class="flashcard-box" data-card-id="{card_data.get('card_id')}">
      <div class="flashcard-question">{card_data.get('question')}</div>
      <div class="flashcard-answer hidden">{card_data.get('answer')}</div>
    </div>
    """
