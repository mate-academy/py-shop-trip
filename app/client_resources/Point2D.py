from __future__ import annotations
from math import sqrt


class Point2d:
    def __init__(self, coordinates: list) -> None:
        self.x = coordinates[0]
        self.y = coordinates[1]

    def distance_to(self, other: Point2d) -> float:
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return sqrt(dx * dx + dy * dy)
