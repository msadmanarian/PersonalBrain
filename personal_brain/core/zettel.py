import datetime
import re

def generate_zettel_id(timestamp: Optional[float] = None) -> str:
    """Generate canonical YYYYMMDDHHMMSS Zettelkasten identifier."""
    dt = datetime.datetime.fromtimestamp(timestamp) if timestamp else datetime.datetime.now()
    return dt.strftime("%Y%m%d%H%M%S")

def parse_luhmann_index(index_str: str) -> list:
    """Parse hierarchical Luhmann foliation sequence (e.g. '1.1a2b')."""
    tokens = re.findall(r"(\d+|[a-zA-Z]+)", index_str)
    return tokens
