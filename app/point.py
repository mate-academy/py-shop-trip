from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Point:
    x_coord: int
    y_coord: int

    def calculate_distance(self, other: Point) -> float:
        return round(
            (
                (other.x_coord - self.x_coord) ** 2
                + (other.y_coord - self.y_coord) ** 2
            )
            ** 0.5, 2
        )
