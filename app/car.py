import math
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def trip_cost(self,
                  customer_location: list,
                  shop_location: list,
                  fuel_cost: float
                  ) -> float:

        path = math.dist(customer_location, shop_location)
        return path * (self.fuel_consumption / 100) * fuel_cost
