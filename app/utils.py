def format_price(price: float) -> str:
    return f"{float(price):.2f}".rstrip("0").rstrip(".")
