from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType

PRODUCTIVITY_NODES = [
    BrainNode(
        title="Zettelkasten Method",
        content="Niklas Luhmann's slip-box note-taking methodology based on atomic notes, persistent identifiers, bi-directional linking, and emergent structure rather than rigid folders. Q:: What makes a note atomic in Zettelkasten? A:: It contains exactly one coherent idea, expressed in the author's own words with outgoing references.",
        node_type=NodeType.CONCEPT,
        tags=["productivity", "pkm", "zettelkasten"]
    ),
    BrainNode(
        title="Getting Things Done (GTD)",
        content="David Allen's productivity framework: Capture, Clarify, Organize, Reflect, Engage. Emphasizes clearing the mental workspace into an external trusted system. Connected to [[Working Memory & Miller's Law]].",
        node_type=NodeType.CONCEPT,
        tags=["productivity", "gtd", "task-management"]
    ),
    BrainNode(
        title="Spaced Repetition & SuperMemo",
        content="Learning technique that incorporates increasing intervals between subsequent reviews of previously learned material to exploit the psychological spacing effect. Core algorithm: [[SM-2]].",
        node_type=NodeType.CONCEPT,
        tags=["learning", "memory", "spaced-repetition"]
    ),
]
