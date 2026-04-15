def format_money(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return str(value)
