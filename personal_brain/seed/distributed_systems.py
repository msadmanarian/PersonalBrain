from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType

DISTRIBUTED_NODES = [
    BrainNode(
        title="Raft Consensus Algorithm",
        content="A consensus algorithm designed to be understandable and safe for replicated state machines. Elects a leader, replicates log entries, and maintains state consistency across server crashes. See [[CAP Theorem]]. Q:: How does Raft maintain consensus? A:: Via randomized leader election, heartbeats, and strict majority log entry replication.",
        node_type=NodeType.CONCEPT,
        tags=["distributed-systems", "consensus", "fault-tolerance"]
    ),
    BrainNode(
        title="Eventual Consistency",
        content="A consistency model used in distributed computing where if no new updates are made, all replicas will eventually return the last updated value. Used in Dynamo-style databases. Relates to [[CAP Theorem]].",
        node_type=NodeType.CONCEPT,
        tags=["distributed-systems", "database", "availability"]
    ),
]
