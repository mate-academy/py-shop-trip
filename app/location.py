from __future__ import annotations


class Location:
    def __init__(self, x_axis: int, y_axis: int) -> None:
        self.x = x_axis
        self.y = y_axis

    def calculate_distance(self, other: Location) -> float:
        distance = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

        return distance
