from __future__ import annotations

from typing import List


class Point:
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    @classmethod
    def create_point(cls, points: List[int, int]) -> Point:
        x, y = points
        return cls(x, y)

    def get_distance(self, other: Point) -> int | float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"x_axis: {self.x}; y_axis: {self.y}"
