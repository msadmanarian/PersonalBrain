import os
from typing import List
from personal_brain.core.node import BrainNode

def export_vault_to_markdown_files(nodes: List[BrainNode], output_dir: str) -> int:
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for n in nodes:
        safe_name = "".join(c for c in n.title if c.isalnum() or c in (' ', '_', '-')).rstrip()
        filename = f"{safe_name}.md"
        filepath = os.path.join(output_dir, filename)
        tags_str = ", ".join(n.tags)
        content = f"---\nid: {n.node_id}\ntitle: {n.title}\ntype: {n.node_type.value}\ntags: [{tags_str}]\n---\n\n# {n.title}\n\n{n.content}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
    return count
