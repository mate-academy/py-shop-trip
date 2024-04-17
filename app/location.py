from __future__ import annotations


class Location:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def calculate_distance(self, other: Location) -> float:
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Location: ({self.x}, {self.y})"
