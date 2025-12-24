from dataclasses import dataclass
from math import sqrt


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def trip_consumption(self, dot_a: list, dot_b: list) -> float or bool:
        xa = dot_a[0]
        ya = dot_a[1]
        xb = dot_b[0]
        yb = dot_b[1]
        distance = sqrt((xb - xa) ** 2 + (yb - ya) ** 2) * 2
        consumption = distance / 100 * self.fuel_consumption
        return consumption
