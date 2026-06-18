from __future__ import annotations
from math import sqrt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.shop import Shop


class Customer:

    def __init__(self,
                 name: str,
                 location: list,
                 product_cart: dict,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.home_location = location
        self.location = location
        self.product_cart = product_cart
        self.money = money
        self.car = car

    def calculate_distance(self, shop: "Shop") -> float:
        x1 = self.home_location[0]
        y1 = self.home_location[1]
        x2 = shop.location[0]
        y2 = shop.location[1]
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def move_to_shop(self, shop: "Shop") -> None:
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}")

    def move_to_home(self) -> None:
        self.location = self.home_location
        print(f"{self.name} rides home")
