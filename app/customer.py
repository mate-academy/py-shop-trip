from typing import List

from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        initial_location: List[int],
        money: int,
        car: Car = None,
        product_cart: dict = None,
        products_bought: dict = None
    ) -> None:
        self.name = name
        self.initial_location = initial_location
        self.money = money
        self.car = car
        self.product_cart = {} if None else product_cart
        self.products_bought = {} if None else products_bought
