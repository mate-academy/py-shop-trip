import math


def distance(loc1: list, loc2: list) -> float:
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)
