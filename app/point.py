from __future__ import annotations

import math


class Point:
    def __init__(self, cor_x: int, cor_y: int) -> None:
        self.x = cor_x
        self.y = cor_y

    @classmethod
    def create_from_location(cls, location: list[int]) -> Point:
        return cls(cor_x=location[0], cor_y=location[1])

    def calculate_distance_to(self, destination: Point) -> float:
        return math.sqrt(
            math.pow(destination.x - self.x, 2)
            + math.pow(destination.y - self.y, 2)
        )
