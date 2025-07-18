from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Location:
    x_coord: int
    y_coord: int

    def distance(self, other: Location) -> float:
        return (
            (self.x_coord - other.x_coord) ** 2
            + (self.y_coord - other.y_coord) ** 2
        ) ** 0.5
