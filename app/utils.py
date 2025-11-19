def format_number(number: int | float) -> str:
    str_number = str(number)
    if "." in str_number:
        whole, frac = str_number.split(".", 1)
        if len(frac) > 2:
            return f"{float(number):.2f}"  # noqa: E231
        return str_number
    return str_number
