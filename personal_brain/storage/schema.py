MIGRATION_V1 = """
CREATE TABLE IF NOT EXISTS nodes (
    node_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    node_type TEXT NOT NULL,
    tags TEXT,
    created_at REAL NOT NULL,
    updated_at REAL NOT NULL,
    metadata TEXT,
    salience REAL DEFAULT 0.5
);

CREATE TABLE IF NOT EXISTS edges (
    source_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    edge_type TEXT NOT NULL,
    weight REAL DEFAULT 1.0,
    label TEXT,
    created_at REAL NOT NULL,
    metadata TEXT,
    PRIMARY KEY (source_id, target_id, edge_type),
    FOREIGN KEY (source_id) REFERENCES nodes (node_id) ON DELETE CASCADE,
    FOREIGN KEY (target_id) REFERENCES nodes (node_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS review_cards (
    card_id TEXT PRIMARY KEY,
    node_id TEXT NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    repetitions INTEGER DEFAULT 0,
    interval_days REAL DEFAULT 1.0,
    ease_factor REAL DEFAULT 2.5,
    next_review_at REAL NOT NULL,
    last_reviewed_at REAL,
    leech_count INTEGER DEFAULT 0,
    FOREIGN KEY (node_id) REFERENCES nodes (node_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes (node_type);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges (source_id);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges (target_id);
CREATE INDEX IF NOT EXISTS idx_cards_review ON review_cards (next_review_at);
"""

def initialize_database(db_manager):
    cursor = db_manager.get_cursor()
    cursor.executescript(MIGRATION_V1)
    db_manager.conn.commit()
