import math


def calculate_distance(point1: tuple, point2: tuple) -> float:
    distance = (
        math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2))
    return round(distance, 2)
