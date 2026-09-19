import re
from typing import List, Set

WIKILINK_PATTERN = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")

def extract_wikilinks(markdown_text: str) -> List[str]:
    """Extract all target note titles referenced via [[wikilink]]."""
    matches = WIKILINK_PATTERN.findall(markdown_text)
    return [m[0].strip() for m in matches if m[0].strip()]

def replace_wikilinks_with_html(markdown_text: str, link_prefix: str = "#/node/") -> str:
    """Convert [[Target|Alias]] into HTML anchor links."""
    def _repl(match):
        target = match.group(1).strip()
        alias = match.group(2).strip() if match.group(2) else target
        return f'<a href="{link_prefix}{target}" class="brain-link">{alias}</a>'
    return WIKILINK_PATTERN.sub(_repl, markdown_text)
