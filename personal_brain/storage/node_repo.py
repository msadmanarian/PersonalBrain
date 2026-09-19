import json
import time
from typing import List, Optional, Dict, Any
from personal_brain.core.node import BrainNode
from personal_brain.core.types import NodeType

class NodeRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def insert(self, node: BrainNode) -> str:
        cursor = self.db.get_cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO nodes (node_id, title, content, node_type, tags, created_at, updated_at, metadata, salience)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                node.node_id,
                node.title,
                node.content,
                node.node_type.value,
                json.dumps(node.tags),
                node.created_at,
                node.updated_at,
                json.dumps(node.metadata),
                node.salience,
            )
        )
        self.db.conn.commit()
        return node.node_id

    def get_by_id(self, node_id: str) -> Optional[BrainNode]:
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM nodes WHERE node_id = ?", (node_id,))
        row = cursor.fetchone()
        if not row:
            return None
        return BrainNode(
            node_id=row["node_id"],
            title=row["title"],
            content=row["content"],
            node_type=NodeType(row["node_type"]),
            tags=json.loads(row["tags"] or "[]"),
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            metadata=json.loads(row["metadata"] or "{}"),
            salience=row["salience"],
        )

    def list_all(self, limit: int = 100) -> List[BrainNode]:
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM nodes ORDER BY updated_at DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        return [
            BrainNode(
                node_id=r["node_id"],
                title=r["title"],
                content=r["content"],
                node_type=NodeType(r["node_type"]),
                tags=json.loads(r["tags"] or "[]"),
                created_at=r["created_at"],
                updated_at=r["updated_at"],
                metadata=json.loads(r["metadata"] or "{}"),
                salience=r["salience"],
            )
            for r in rows
        ]

    def delete(self, node_id: str) -> bool:
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM nodes WHERE node_id = ?", (node_id,))
        self.db.conn.commit()
        return cursor.rowcount > 0
