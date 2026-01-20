from __future__ import annotations


class Location:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self._x_coord = x_coord
        self._y_coord = y_coord

    @property
    def x_coord(self) -> int:
        return self._x_coord

    @property
    def y_coord(self) -> int:
        return self._y_coord

    def __repr__(self) -> str:
        return f"[{self.x_coord}, {self.y_coord}]"

    def get_distance(self, other: Location) -> float:
        return (
            (other.x_coord - self.x_coord) ** 2
            + (other.y_coord - self.y_coord) ** 2
        ) ** 0.5
