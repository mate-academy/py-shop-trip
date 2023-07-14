from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Location:
    x_cord: int
    y_cord: int

    def __sub__(self, other: Location) -> float:
        vector_x = self.x_cord - other.x_cord
        vector_y = self.y_cord - other.y_cord
        distance = (vector_x ** 2 + vector_y ** 2) ** .5
        return distance
