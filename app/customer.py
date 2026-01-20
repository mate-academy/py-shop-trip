import math
from app.car import Car


class Customer:
    def __init__(self, name: str,
                 money: float,
                 location: list,
                 car: Car,
                 product_cart: dict) -> None:
        self.name = name
        self.money = money
        self.location = location  # [x, y]
        self.car = car
        self.product_cart = product_cart

    def distance_to(self, shop_location: list) -> float:
        """Calculate Euclidean distance between customer and shop location"""
        return math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )
