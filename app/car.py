from dataclasses import dataclass
import math


@dataclass
class Car:
    brand: str
    fuel_consumption: int
    fuel_price: float

    def trip_cost(self, customer_loc: list, shop_loc: list) -> float:
        distance = math.sqrt(
            (customer_loc[0] - shop_loc[0])**2
            + (customer_loc[1] - shop_loc[1])**2
        )
        return distance * self.fuel_consumption / 100 * self.fuel_price
