from __future__ import annotations
import math


class Point:
    def __init__(self, location: list) -> None:
        self.x = location[0]
        self.y = location[1]

    def calculate_distance(self, point: Point) -> float:
        result = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return round(result, 2)
