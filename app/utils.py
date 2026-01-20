import datetime


def get_datetime() -> str:
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def float_to_int(number: int | float) -> int | float:
    if isinstance(number, float) and number.is_integer():
        return int(number)
    return number


def round_to_2(number: float) -> float:
    return round(number, 2)
