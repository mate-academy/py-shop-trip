import math
from typing import Tuple


def distance(loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
    return math.dist(loc1, loc2)
