import math
from typing import List


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand: str = brand
        self.fuel_consumption: float = fuel_consumption

    def cost_of_fuel_all_way(
        self, customer_location: List[float], shop_location: List[float]
    ) -> float:
        distance: float = math.sqrt(
            (customer_location[0] - shop_location[0]) ** 2
            + (customer_location[1] - shop_location[1]) ** 2
        )
        return (distance / 100) * self.fuel_consumption * 2
