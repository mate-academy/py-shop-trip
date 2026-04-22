import math
from typing import Tuple


def get_distance(
        loc1: Tuple[float, float],
        loc2: Tuple[float, float]
) -> float:
    return math.hypot(loc1[0] - loc2[0], loc1[1] - loc2[1])
