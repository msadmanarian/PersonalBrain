from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType

AI_NODES = [
    BrainNode(
        title="Dual-Process Theory",
        content="Daniel Kahneman's cognitive framework dividing mental processes into System 1 (fast, instinctive, emotional, heuristic) and System 2 (slow, deliberative, logical, effortful). Highly relevant to [[Autonomous Agents]] and [[Cognitive Architecture]]. Q:: Contrast System 1 and System 2. A:: System 1 is fast, heuristic, and automatic; System 2 is slow, deliberative, and logical.",
        node_type=NodeType.CONCEPT,
        tags=["cognitive-science", "psychology", "kahneman"]
    ),
    BrainNode(
        title="Working Memory & Miller's Law",
        content="George A. Miller's 1956 finding that short-term cognitive capacity is bounded to 7 plus or minus 2 discrete chunks of information. Central to personal productivity and interface design. Linked to [[Spaced Repetition]] and [[Zettelkasten]].",
        node_type=NodeType.CONCEPT,
        tags=["psychology", "memory", "cognitive-load"]
    ),
    BrainNode(
        title="Tree of Thoughts Reasoning",
        content="An advanced framework for language model problem solving where models explore multiple reasoning trajectories, evaluate intermediate thoughts, and backtrack when necessary. Connects [[Dual-Process Theory]] with MCTS search.",
        node_type=NodeType.CONCEPT,
        tags=["ai", "llm", "reasoning"]
    ),
]
