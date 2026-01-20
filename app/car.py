from dataclasses import dataclass

import math


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_road_cost(
            self, customer_point: list, shop_point: list, fuel_price: float
    ) -> float:
        x1, y1 = customer_point
        x2, y2 = shop_point
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return fuel_price * (self.fuel_consumption / 100) * (distance * 2)
