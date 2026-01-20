def format_price(price: float) -> str:
    rounded_price = round(price, 2)
    rounded_price = float(rounded_price)
    return (
        str(int(rounded_price))
        if rounded_price.is_integer()
        else str(rounded_price)
    )
