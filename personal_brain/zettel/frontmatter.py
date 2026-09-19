import re
from typing import Dict, Any, Tuple

FRONTMATTER_REGEX = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def parse_frontmatter(raw_text: str) -> Tuple[Dict[str, Any], str]:
    match = FRONTMATTER_REGEX.match(raw_text)
    if not match:
        return {}, raw_text
    fm_block = match.group(1)
    body = raw_text[match.end():]
    metadata = {}
    for line in fm_block.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            metadata[key.strip()] = val.strip()
    return metadata, body
