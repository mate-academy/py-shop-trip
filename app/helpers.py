def format_float(number: float) -> str:
    return f"{int(number)}" if number.is_integer() else f"{number}"
