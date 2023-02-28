import math
from dataclasses import dataclass
from typing import List


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    location: List[int]

    def trip_fuel_cost(
            self,
            shop_location: List[int],
            fuel_price: float
    ) -> float:
        trip_distance = math.dist(self.location, shop_location) * 2
        return round(
            (trip_distance * self.fuel_consumption)
            / 100 * fuel_price, 2
        )
