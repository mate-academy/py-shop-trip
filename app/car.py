from math import sqrt
from typing import Any


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def calculate_trip_cost(
            customer: Any,
            shop: Any,
            fuel_price: float
    ) -> float:
        x1, y1 = customer.location
        x2, y2 = shop.location
        distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        trip_fuel_cost = (
            (distance / 100) * customer.car.fuel_consumption * fuel_price * 2
        )
        return trip_fuel_cost
