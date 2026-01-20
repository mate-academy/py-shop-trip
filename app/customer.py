from math import sqrt
from typing import Any


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: Any
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(
            self,
            shop: Any,
            fuel_price: float
    ) -> float:
        distance_to_shop = sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        )
        fuel_cost = ((distance_to_shop * 2)
                     * (self.car.fuel_consumption / 100)
                     * fuel_price)
        product_cost = sum(
            shop.products[product] * quantity
            for product, quantity in self.product_cart.items()
        )
        total_cost = fuel_cost + product_cost
        return round(total_cost, 2)
