from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType

CS_NODES = [
    BrainNode(
        title="Turing Completeness",
        content="A system of data-manipulation rules is said to be [[Turing Completeness|Turing Complete]] if it can simulate any single-taped Turing machine. Fundamental to [[Theory of Computation]]. Q:: What is Turing Completeness? A:: The capability of a computational system to simulate any arbitrary Turing machine.",
        node_type=NodeType.CONCEPT,
        tags=["computer-science", "theory", "automata"]
    ),
    BrainNode(
        title="CAP Theorem",
        content="Brewer's conjecture states that in any distributed data store, one can only achieve two of three guarantees: Consistency, Availability, and Partition Tolerance. In practice, networks are always subject to partitions, forcing a trade-off between Consistency and Availability. See [[Distributed Systems]].",
        node_type=NodeType.CONCEPT,
        tags=["distributed-systems", "architecture", "database"]
    ),
    BrainNode(
        title="ACID Transactions",
        content="Guarantees for reliable database transactions: Atomicity (all or nothing), Consistency (preserves invariants), Isolation (concurrency control), and Durability (persisted on disk). Contrast with BASE in [[Distributed Systems]]. Q:: What does ACID stand for? A:: Atomicity, Consistency, Isolation, Durability.",
        node_type=NodeType.CONCEPT,
        tags=["database", "storage", "sql"]
    ),
]
