import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def distance_calculator(
            shop_location: list[int],
            customer_location: list[int]
    ) -> float:
        return math.sqrt(
            (shop_location[0] - customer_location[0])
            ** 2 + (shop_location[1] - customer_location[1]) ** 2
        )
