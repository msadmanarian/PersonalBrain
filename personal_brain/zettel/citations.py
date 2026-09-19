from typing import Dict, Any

def format_citation(author: str, year: int, title: str, source: str) -> str:
    return f"@{author.lower().replace(' ', '')}{year}: *{title}*. {source}."
