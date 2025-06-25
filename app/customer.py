import math
from app.car import Car
from typing import Any


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def _distance(self, other_location: list) -> float:
        return math.dist(self.location, other_location)

    def calculate_trip_cost(self, shop: Any, fuel_price: float) -> float:
        distance_to_store = self._distance(shop.location)
        fuel_cost = self.car.get_trip_cost(distance_to_store * 2, fuel_price)

        products_cost = 0
        for product_name, quantity in self.product_cart.items():
            if product_name in shop.products:
                products_cost += shop.products[product_name] * quantity

        return fuel_cost + products_cost
