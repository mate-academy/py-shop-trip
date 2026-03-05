def format_money(value: float) -> str:
    formatted_value = int(value) \
        if value % 1 == 0 \
        else round(value, 2)
    return str(formatted_value)
