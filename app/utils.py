import math


def distance(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return math.dist(p1, p2)


def format_money(value: float) -> str:
    formatted = format(value, ".2f")
    return formatted.rstrip("0").rstrip(".")
