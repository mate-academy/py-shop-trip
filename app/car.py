from math import sqrt


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def total_consumption(
            self,
            start: list,
            end: list
    ) -> float:
        distance = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        return 2 * distance * self.fuel_consumption / 100
