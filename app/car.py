from math import sqrt
from typing import Any


class Car:
    FUEL_PRICE = None

    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculates_fuel_cost_per_km(self) -> float:
        return (self.fuel_consumption * Car.FUEL_PRICE) / 100

    @staticmethod
    def calculates_trip_cost_to_shop(customer: Any, shop: Any) -> int | float:
        trip_cost_to_shop = (
            sqrt(
                (shop.location[0] - customer.location[0]) ** 2
                + (shop.location[1] - customer.location[1]) ** 2
            )
            * customer.car.calculates_fuel_cost_per_km()
        )
        return trip_cost_to_shop * 2
