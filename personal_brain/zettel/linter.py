from typing import List, Dict, Set
from personal_brain.core.node import BrainNode
from personal_brain.graph.wikilinks import extract_wikilinks

def audit_vault_integrity(nodes: List[BrainNode]) -> Dict[str, Any]:
    titles = {n.title.lower(): n.node_id for n in nodes}
    broken_links = []
    for n in nodes:
        links = extract_wikilinks(n.content)
        for link in links:
            if link.lower() not in titles:
                broken_links.append({"source": n.title, "broken_target": link})
    return {
        "total_notes": len(nodes),
        "broken_links_count": len(broken_links),
        "broken_links": broken_links,
    }
