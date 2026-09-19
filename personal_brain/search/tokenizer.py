import re
from typing import List

def tokenize(text: str) -> List[str]:
    """Extract lowercased alphanumeric tokens from text."""
    return [w.lower() for w in re.findall(r"\b[a-zA-Z0-9_]{2,}\b", text)]
