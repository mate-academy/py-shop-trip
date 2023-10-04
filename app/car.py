from dataclasses import dataclass
from math import sqrt


@dataclass
class Car:
    brand: str
    fuel_consumption: int
    fuel_price: float

    @staticmethod
    def trip_distance(customer_loc: list, shop_loc: list) -> float:
        distance = sqrt(
            (customer_loc[0] - shop_loc[0])**2
            + (customer_loc[1] - shop_loc[1])**2
        )
        return distance
