import json
from typing import List, Tuple
from personal_brain.core.edge import BrainEdge
from personal_brain.core.types import EdgeType

class EdgeRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def insert(self, edge: BrainEdge) -> None:
        cursor = self.db.get_cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO edges (source_id, target_id, edge_type, weight, label, created_at, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                edge.source_id,
                edge.target_id,
                edge.edge_type.value,
                edge.weight,
                edge.label,
                edge.created_at,
                json.dumps(edge.metadata),
            )
        )
        self.db.conn.commit()

    def get_outbound(self, source_id: str) -> List[BrainEdge]:
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM edges WHERE source_id = ?", (source_id,))
        return [
            BrainEdge(
                source_id=r["source_id"],
                target_id=r["target_id"],
                edge_type=EdgeType(r["edge_type"]),
                weight=r["weight"],
                label=r["label"] or "",
                created_at=r["created_at"],
                metadata=json.loads(r["metadata"] or "{}"),
            )
            for r in cursor.fetchall()
        ]

    def get_inbound(self, target_id: str) -> List[BrainEdge]:
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM edges WHERE target_id = ?", (target_id,))
        return [
            BrainEdge(
                source_id=r["source_id"],
                target_id=r["target_id"],
                edge_type=EdgeType(r["edge_type"]),
                weight=r["weight"],
                label=r["label"] or "",
                created_at=r["created_at"],
                metadata=json.loads(r["metadata"] or "{}"),
            )
            for r in cursor.fetchall()
        ]

    def list_all(self) -> List[BrainEdge]:
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM edges")
        return [
            BrainEdge(
                source_id=r["source_id"],
                target_id=r["target_id"],
                edge_type=EdgeType(r["edge_type"]),
                weight=r["weight"],
                label=r["label"] or "",
                created_at=r["created_at"],
                metadata=json.loads(r["metadata"] or "{}"),
            )
            for r in cursor.fetchall()
        ]
