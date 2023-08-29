import math
from app.car import Car


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"])

    @staticmethod
    def calculate_distance(point1: list, point2: list) -> float:
        x1, y1 = point1
        x2, y2 = point2
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance

    @staticmethod
    def calculate_fuel_cost(
            distance: float,
            fuel_price: float,
            fuel_consumption: float
    ) -> float:
        return fuel_consumption * fuel_price * (distance / 100)
