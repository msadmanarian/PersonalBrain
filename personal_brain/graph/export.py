from typing import List, Dict, Any

def export_to_dot(nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]]) -> str:
    """Export knowledge graph to Graphviz DOT specification."""
    lines = ["digraph PersonalBrain {", "  node [shape=box, style=rounded, fontname=Helvetica];"]
    for n in nodes:
        safe_title = n.get("title", "").replace('"', '\"')
        lines.append(f'  "{n["node_id"]}" [label="{safe_title}"];')
    for e in edges:
        lines.append(f'  "{e["source_id"]}" -> "{e["target_id"]}" [label="{e.get("edge_type", "")}"];')
    lines.append("}")
    return "\n".join(lines)
