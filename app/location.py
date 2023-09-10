from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass
class Location:
    x_coordinate: int
    y_coordinate: int

    @classmethod
    def deserialize_from_list(cls, info: list) -> Location:
        return cls(info[0], info[1])

    def find_distance(self, other: Location) -> float:
        return math.dist(
            [self.x_coordinate, self.y_coordinate],
            [other.x_coordinate, other.y_coordinate]
        )
