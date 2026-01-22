def format_money(amount: float) -> str:
    if isinstance(amount, int):
        return str(amount)

    if isinstance(amount, float) and amount.is_integer():
        return str(int(amount))

    formatted = f"{amount: .2f}".lstrip()
    return formatted.rstrip("0").rstrip(".")
