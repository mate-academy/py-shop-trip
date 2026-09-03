def format_float(val):
    return f"{int(val)}" if val.is_integer() else f"{val}"
