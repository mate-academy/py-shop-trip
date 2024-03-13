from math import sqrt


def calculate_distance(location1: tuple, location2: tuple) -> float:
    x1, y1 = location1
    x2, y2 = location2
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
