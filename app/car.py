import math
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def count_fuel_price(
            self,
            fuel_price: float,
            customer_loc: list[int],
            shop_loc: list[int]
    ) -> float:
        distance = math.dist(customer_loc, shop_loc)
        fuel = self.fuel_consumption / 100
        return fuel * fuel_price * distance
