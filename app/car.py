from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def get_trip_cost(self, distance: float, fuel_price: float) -> float:
        return (distance / 100) * self.fuel_consumption * fuel_price

    @staticmethod
    def get_distance(
            customer_location: List[int],
            shop_location: List[int]
    ) -> float:
        return ((customer_location[0] - shop_location[0]) ** 2
                + (customer_location[1] - shop_location[1]) ** 2) ** 0.5
