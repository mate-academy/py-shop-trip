import math
from typing import List, Any

from app.car import Car


class Customer:
    def __init__(self, customer_config: dict) -> None:
        self.name: str = customer_config["name"]
        self.product_cart: dict = customer_config["product_cart"]
        self.location: List[int] = customer_config["location"]
        self.money: int | float = customer_config["money"]
        self.car: Car = Car(
            customer_config["car"]["brand"],
            customer_config["car"]["fuel_consumption"]
        )

    def fuel_costs_calculation(self, place: Any, fuel_price: float) -> float:
        distance = math.dist(self.location, place.location)
        fuel_consumption = self.car.fuel_consumption / 100
        back_and_forth_coefficient = 2

        return round(
            distance * back_and_forth_coefficient
            * (fuel_consumption * fuel_price), 2
        )
