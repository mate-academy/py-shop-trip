def format_price(price: float) -> str:
    price = float(price)
    strip = f"{price:.2f}".rstrip("0").rstrip(".")
    return strip
