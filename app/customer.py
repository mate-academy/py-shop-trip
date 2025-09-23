from __future__ import annotations
from car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: list[str, int],
        location: list[float],
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = list(location)
