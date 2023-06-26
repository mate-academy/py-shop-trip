import math

from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    location: list[int]

    def fuel_price(self, shop_location: list[int], fuel_price: float) -> float:
        cost = math.dist(self.location, shop_location) * 2
        cost = cost * (self.fuel_consumption / 100)

        return round(cost * fuel_price, 2)

    def __repr__(self) -> str:
        return self.brand
