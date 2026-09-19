from typing import List
from personal_brain.core.node import BrainNode

def generate_map_of_content(topic: str, nodes: List[BrainNode]) -> str:
    """Compile an automated Map of Content (MOC) index note for a given topic."""
    lines = [
        f"# Map of Content: {topic}",
        "",
        f"Curated index of all permanent notes and concepts under [[{topic}]].",
        "",
        "## Index of Notes",
    ]
    for n in sorted(nodes, key=lambda x: x.title):
        lines.append(f"- [[{n.title}]] — *{n.node_type.value}*")
    return "\n".join(lines)
