import dataclasses
import math
from typing import Dict
from decimal import Decimal
from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    products: Dict[str, int]
    location: list[int]
    money: Decimal
    car: Car

    @staticmethod
    def calculate_distance(
            point1: list[int],
            point2: list[int]
    ) -> float:
        x1, y1 = point1
        x2, y2 = point2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def calculate_trip_cost(
            self,
            shop_location: list[int],
            fuel_price: Decimal
    ) -> Decimal:
        distance = self.calculate_distance(shop_location, self.location)
        total_cost = (distance / 100) * self.car.consumption * fuel_price
        return Decimal(total_cost)
