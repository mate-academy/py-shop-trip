import math


def distance(point_a: list[int], point_b: list[int]) -> float:
    return math.sqrt(
        (point_a[0] - point_b[0]) ** 2
        + (point_a[1] - point_b[1]) ** 2
    )
