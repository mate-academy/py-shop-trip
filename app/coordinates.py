from __future__ import annotations

from dataclasses import dataclass, field


class Coordinate:
    def __set_name__(self, owner: type, coordinate: str) -> None:
        self.coordinate = coordinate[0]

    def __get__(self, instance: Coordinates, owner: type) -> int:
        return getattr(instance, self.coordinate)

    def __set__(self, instance: Coordinates, value: int) -> None:
        setattr(instance, self.coordinate, value)


@dataclass
class Coordinates:
    x_coord: int = field(default=Coordinate(), repr=False)
    y_coord: int = field(default=Coordinate(), repr=False)

    def distance(self, other: Coordinates) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
