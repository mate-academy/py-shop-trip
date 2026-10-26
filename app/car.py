from math import hypot
from typing import Sequence


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self, distance: float, fuel_price: float) -> float:
        return distance * self.fuel_consumption / 100 * fuel_price

    @staticmethod
    def distance(
        first_location: Sequence[float], second_location: Sequence[float]
    ) -> float:
        return hypot(
            first_location[0] - second_location[0],
            first_location[1] - second_location[1],
        )
