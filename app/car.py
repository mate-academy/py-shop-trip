import math
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_price(self,
                             fuel_price: float,
                             customer_location: list[int],
                             shop_location: list[int]) -> float:
        distance = math.dist(customer_location, shop_location) * 2
        return round((self.fuel_consumption / 100 * fuel_price * distance), 2)
