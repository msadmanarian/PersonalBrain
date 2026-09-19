def generate_child_index(parent_index: str, sibling_count: int) -> str:
    """Generates next alphanumeric Luhmann foliation (e.g., '1.1' -> '1.1a', '1.1a1')."""
    if not parent_index:
        return str(sibling_count + 1)
    last_char = parent_index[-1]
    if last_char.isdigit():
        char = chr(ord('a') + sibling_count)
        return f"{parent_index}{char}"
    else:
        return f"{parent_index}{sibling_count + 1}"
