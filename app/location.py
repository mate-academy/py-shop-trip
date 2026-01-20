from __future__ import annotations


class Location:
    def __init__(self, x_: int, y_: int) -> None:
        self.x = x_
        self.y = y_

    def get_distance_to(self, other: Location) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
