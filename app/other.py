from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass
class Location:
    x_coordinate: int
    y_coordinate: int

    @staticmethod
    def deserialize_from_list(info: list) -> Location:
        return Location(info[0], info[1])

    def find_distance(self, other: Location) -> float:
        return math.dist(
            [self.x_coordinate, self.y_coordinate],
            [other.x_coordinate, other.y_coordinate]
        )


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @staticmethod
    def deserialize_from_dict(info: dict) -> Car:
        return Car(info["brand"], info["fuel_consumption"])
