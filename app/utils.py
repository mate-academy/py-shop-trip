import math
from typing import List


def distance(point1: List[float], point2: List[float]) -> float:
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    )
