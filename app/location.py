from __future__ import annotations


class Location:
    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self._x = x_value
        self._y = y_value

    @property
    def x(self) -> int | float:
        return self._x

    @property
    def y(self) -> int | float:
        return self._y

    def distance_to(self, other: Location) -> float:
        return ((other._x - self._x) ** 2 + (other._y - self._y) ** 2) ** 0.5

    @staticmethod
    def from_list(location_list: list) -> Location:
        return Location(
            x_value=location_list[0],
            y_value=location_list[1]
        )

    def __repr__(self) -> str:
        return f"Location(x={self._x}, y={self._y})"
