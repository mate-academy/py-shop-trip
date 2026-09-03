def format_float(number: float) -> str:
    return f"{int(number)}" if number.is_integer() else f"{number}"


def format_money(number: float) -> str:
    return f"{round(number, 2):g}"
