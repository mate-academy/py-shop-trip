import math

from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def count_fuel_price(
        self,
        fuel_price: float,
        customer_location: list[int],
        shop_location: list[int]
    ) -> float:
        distance = math.dist(customer_location, shop_location)
        fuel_consumption_per_km = self.fuel_consumption / 100

        return fuel_consumption_per_km * fuel_price * distance
