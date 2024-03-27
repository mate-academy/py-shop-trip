from __future__ import annotations


class Coordinate2D:
    def __init__(self, location: list[int]) -> None:
        self.x = location[0]
        self.y = location[1]

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def distance_to(self, other_coordinate: Coordinate2D) -> int | float:
        x_move = self.x - other_coordinate.x
        y_move = self.y - other_coordinate.y
        return (x_move ** 2 + y_move ** 2) ** 0.5
