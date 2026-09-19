from typing import Dict, List

def apply_tag_boost(scores: Dict[str, float], doc_tags: Dict[str, List[str]], target_tag: str, boost: float = 1.3) -> Dict[str, float]:
    boosted = {}
    target_clean = target_tag.lower()
    for doc_id, score in scores.items():
        tags = [t.lower() for t in doc_tags.get(doc_id, [])]
        if target_clean in tags:
            boosted[doc_id] = round(score * boost, 4)
        else:
            boosted[doc_id] = score
    return boosted
