from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType

PHILOSOPHY_NODES = [
    BrainNode(
        title="First Principles Thinking",
        content="Aristotelian mode of reasoning that boils a problem down to its most fundamental, immutable truths and reasons upward from there, avoiding analogical reasoning traps. Connects to [[Scientific Method]] and [[Problem Solving]].",
        node_type=NodeType.CONCEPT,
        tags=["philosophy", "mental-models", "reasoning"]
    ),
    BrainNode(
        title="Dialectical Method",
        content="Hegelian discourse between opposing assertions: Thesis is challenged by Antithesis, resulting in a synthesized truth (Synthesis) that resolves the contradiction. Directly applied in multi-agent research and [[PersonalBrain]].",
        node_type=NodeType.CONCEPT,
        tags=["philosophy", "hegel", "epistemology"]
    ),
]
