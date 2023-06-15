from __future__ import annotations
from dataclasses import dataclass
from math import sqrt


@dataclass
class Location:
    x_axis: int
    y_axis: int

    def __sub__(self, other: Location) -> float:
        return sqrt(
            (other.x_axis - self.x_axis) ** 2
            + (other.y_axis - self.y_axis) ** 2
        )
