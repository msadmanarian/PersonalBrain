import sqlite3
import os
from typing import Optional

DEFAULT_DB_PATH = os.path.join(os.path.expanduser("~"), ".personal_brain", "brain.sqlite3")

class DatabaseManager:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or DEFAULT_DB_PATH
        if self.db_path != ":memory:" and os.path.dirname(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._enable_wal_mode()

    def _enable_wal_mode(self):
        cursor = self.conn.cursor()
        if self.db_path != ":memory:":
            cursor.execute("PRAGMA journal_mode = WAL;")
            cursor.execute("PRAGMA synchronous = NORMAL;")
        cursor.execute("PRAGMA foreign_keys = ON;")
        self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

    def close(self):
        self.conn.close()
