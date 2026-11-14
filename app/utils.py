def format_amount(amount: float) -> str:
    return f"{amount:.2f}".rstrip("0").rstrip(".")
