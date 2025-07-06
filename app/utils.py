def format_price(price: float) -> str:
    rounded = round(price * 100) / 100
    if rounded == int(rounded):
        return str(int(rounded))
    price_str = str(rounded)
    if price_str.endswith(".0"):
        price_str = price_str[:-2]
    return price_str
