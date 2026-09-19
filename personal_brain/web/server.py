import http.server
import socketserver
import json
import os
import urllib.parse
from personal_brain.storage.db import DatabaseManager
from personal_brain.storage.schema import initialize_database
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.storage.edge_repo import EdgeRepository
from personal_brain.graph.adjacency import AdjacencyGraph
from personal_brain.graph.pagerank import compute_pagerank
from personal_brain.seed.loader import seed_knowledge_base

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

class BrainRequestHandler(http.server.SimpleHTTPRequestHandler):
    db = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/status":
            nodes = NodeRepository(self.db).list_all(limit=1000)
            edges = EdgeRepository(self.db).list_all()
            self._send_json(200, {
                "status": "online",
                "nodes_count": len(nodes),
                "edges_count": len(edges),
            })
        elif parsed.path == "/api/graph":
            nodes = NodeRepository(self.db).list_all(limit=1000)
            edges = EdgeRepository(self.db).list_all()
            self._send_json(200, {
                "nodes": [n.to_dict() for n in nodes],
                "edges": [e.to_dict() for e in edges],
            })
        else:
            super().do_GET()

    def _send_json(self, status: int, data: dict):
        response = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format, *args):
        pass

def run_server(port: int = 8080):
    db = DatabaseManager()
    initialize_database(db)
    seed_knowledge_base(db)
    BrainRequestHandler.db = db
    with socketserver.TCPServer(("", port), BrainRequestHandler) as httpd:
        print(f"[*] PersonalBrain Web Lab running at: http://localhost:{port}")
        httpd.serve_forever()
