import math
from datetime import datetime


def calculate_distance(loc1: list, loc2: list) -> float:
    distance = math.sqrt((loc2[0] - loc1[0])**2 + (loc2[1] - loc1[1])**2)
    return distance


def get_current_time() -> str:
    result = datetime(2021, 1, 4, 12, 33, 41)
    # result = datetime.now()
    result = result.strftime("%d/%m/%Y %H:%M:%S")
    return result


def round2(value: float) -> float:
    new_value = round(value, 2)
    return new_value


def from_float_to_int(value: float) -> int | float:
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value
