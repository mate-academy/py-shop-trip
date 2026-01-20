from dataclasses import dataclass
from math import dist


@dataclass
class Car:
    brand: str
    fuel_consumption: float


@dataclass
class Point:
    x_coord: int
    y_coord: int

    def calc_dist(self, other: "Point") -> float:
        return dist(
            (self.x_coord, self.y_coord),
            (other.x_coord, other.y_coord))
