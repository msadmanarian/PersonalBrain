from personal_brain.search.hybrid import HybridSearchEngine
from personal_brain.storage.node_repo import NodeRepository

def search_cli(db_manager, query: str):
    nodes = NodeRepository(db_manager).list_all(limit=5000)
    docs = {n.node_id: f"{n.title} {n.content}" for n in nodes}
    engine = HybridSearchEngine()
    engine.index(docs)
    return engine.search(query)
