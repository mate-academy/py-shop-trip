from math import sqrt


class Car:

    def __init__(
            self, brand: str,
            fuel_consumption: int | float,
            fuel_price: int | float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def __str__(self) -> str:
        return (f"Brand: {self.brand}, "
                f"fuel consumption: {self.fuel_consumption}")

    def price_for_travel(self, distance: int | float) -> int | float:
        return (self.fuel_consumption / 100 * distance * self.fuel_price) * 2

    @staticmethod
    def distance(point1: list, point2: list) -> int | float:
        return sqrt(
            (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
        )
