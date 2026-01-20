from __future__ import annotations

from math import sqrt


class Location:
    def __init__(self, x_point: int, y_point: int) -> None:
        self.x = x_point
        self.y = y_point

    def calculate_distance(self, other: Location) -> float:
        """Formula for calculating distance between 2 points:
        sqrt((x2 - x1)^2 + (y2 - y1)^2)"""
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    @classmethod
    def get_location(cls, x_point: int, y_point: int) -> Location:
        return cls(x_point, y_point)
