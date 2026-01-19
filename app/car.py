from dataclasses import dataclass
from math import sqrt


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def total_consumption(self, start: list, end: list) -> float:
        distance = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        return round(2 * distance * self.fuel_consumption / 100, 2)
