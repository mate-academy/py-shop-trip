from math import dist


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(
        self,
        first: list[int | float],
        second: list[int | float],
        price: float,
    ) -> float:
        return 2 * dist(first, second) * self.fuel_consumption / 100 * price
