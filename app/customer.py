import math
from dataclasses import dataclass
from typing import Dict, List

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[int]
    money: int
    car: Car

    def calculate_trip_cost(
        self,
        shop_location: List[int],
        fuel_price: float,
    ) -> float:
        distance = math.dist(self.location, shop_location)
        fuel_needed = (distance / 100) * self.car.fuel_consumption
        trip_cost = fuel_needed * fuel_price
        return trip_cost
