import math


def calculate_distance(location1: list, location2: list) -> float:
    x1, y1 = location1
    x2, y2 = location2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_gas_price(
        gas_price: float,
        gas_usage: float,
        distance: float
) -> float:
    return (gas_usage / 100) * gas_price * distance
