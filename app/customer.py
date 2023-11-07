import math
from typing import List

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.products_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = Car(**car)

    def money_count(self) -> None:
        """Prints sum of money customer has"""
        print(f"{self.name} has {self.money} dollars")

    def calculate_distance(self, shop_location: List[int]) -> float:
        """Returns a distance between customer's home and shop"""
        x1, y1 = self.location
        x2, y2 = shop_location
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
