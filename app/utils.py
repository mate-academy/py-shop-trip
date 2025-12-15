def clean_round(number: int | float) -> int | float:
    rounded_number = round(number, 2)
    if rounded_number == int(rounded_number):
        return int(rounded_number)
    return rounded_number
