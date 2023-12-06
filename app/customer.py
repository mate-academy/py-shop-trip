from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    name: str
    location: List[int]
    money: int | float
    car: dict
    product_cart: dict

    def distance(self, shop_dist: object) -> float:
        distance_1 = math.pow((self.location[0] - shop_dist.location[0]), 2)
        distance_2 = math.pow((self.location[1] - shop_dist.location[1]), 2)
        distances = math.sqrt(distance_1 + distance_2)

        return round(distances * 2, 2)

    def calculate_fuel_price(
            self,
            distance: float,
            fuel_price: float
    ) -> int | float:
        car_fuel_consup = self.car["fuel_consumption"]
        fuel_consumption = (distance / 100) * car_fuel_consup * fuel_price
        return fuel_consumption
