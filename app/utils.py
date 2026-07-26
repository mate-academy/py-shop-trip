def format_money(value: float) -> int | float:
    """Round to 2 decimals and drop a zero fraction: 3.0 -> 3."""
    rounded = round(value, 2)

    return int(rounded) if rounded == int(rounded) else rounded
