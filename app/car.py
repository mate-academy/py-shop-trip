import math


class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(
            self,
            coordinates: tuple,
            fuel_price: float
    ) -> float:
        distance = math.dist(coordinates[0], coordinates[1])
        return 2 * distance * self.fuel_consumption / 100 * fuel_price
