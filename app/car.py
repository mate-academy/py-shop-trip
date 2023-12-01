from math import sqrt
from dataclasses import dataclass


@dataclass
class Car:
    fuel_consumption: float

    def get_cost_trip(
            self,
            customer_location: list,
            shop_location: list,
            fuel_price: float
    ) -> float:
        x1, y1 = customer_location
        x2, y2 = shop_location
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 2
        cost_trip = distance * (self.fuel_consumption / 100) * fuel_price
        return round(cost_trip, 2)
