import argparse
import sys
from personal_brain.storage.db import DatabaseManager
from personal_brain.storage.schema import initialize_database
from personal_brain.storage.node_repo import NodeRepository
from personal_brain.seed.loader import seed_knowledge_base
from personal_brain.web.server import run_server

# Force UTF-8 on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def main():
    parser = argparse.ArgumentParser(description="PersonalBrain: AI-Augmented Exocortex CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Initialize database and seed knowledge base")
    subparsers.add_parser("stats", help="Display knowledge graph metrics and count")
    subparsers.add_parser("serve", help="Launch interactive web laboratory")

    search_p = subparsers.add_parser("search", help="Search knowledge notes")
    search_p.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    db = DatabaseManager()
    initialize_database(db)

    if args.command == "init":
        count = seed_knowledge_base(db)
        print(f"[+] Initialized and seeded {count} foundational knowledge nodes.")
    elif args.command == "stats":
        nodes = NodeRepository(db).list_all(limit=5000)
        print("=" * 60)
        print(f"[PERSONALBRAIN STATS]")
        print(f"Total Knowledge Nodes: {len(nodes)}")
        print("=" * 60)
    elif args.command == "serve":
        run_server(port=8080)
    elif args.command == "search":
        nodes = NodeRepository(db).list_all(limit=5000)
        matches = [n for n in nodes if args.query.lower() in n.title.lower() or args.query.lower() in n.content.lower()]
        print(f"Found {len(matches)} matching nodes:")
        for m in matches[:5]:
            print(f"- [{m.title}] ({m.node_type.value})")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
