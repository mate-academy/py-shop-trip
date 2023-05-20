import math
from typing import List
from dataclasses import dataclass
from app.json_reader import data


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @staticmethod
    def create_cars() -> None:
        for customer in data["customers"]:
            Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )

    @staticmethod
    def calculate_fuel_cost(
            customer_location: List[int],
            shop_location: List[int],
            fuel_price: float,
            fuel_consumption: float
    ) -> float:
        distance = math.dist(customer_location, shop_location) * 2
        return round(distance * (fuel_consumption / 100) * fuel_price, 2)
