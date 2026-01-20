import math


def calculate_distance(loc1: list[int], loc2: list[int]) -> float:
    return math.sqrt((loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2)
