from math import hypot


class Location:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self._x = x_coord
        self._y = y_coord

    @property
    def x_coord(self) -> int:
        return self._x

    @property
    def y_coord(self) -> int:
        return self._y

    def distance_to(self, other: Location) -> float | int:
        if not isinstance(other, Location):
            raise TypeError(f"Cannot calculate distance to {type(other)}")
        return hypot(other._x - self._x, other._y - self._y)
