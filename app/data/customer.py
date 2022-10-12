from __future__ import annotations
from math import dist

from app.data.car import Car
from app.data.shop import Shop


class Customer:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs["name"]
        self.product_cart = kwargs["product_cart"]
        self.location = kwargs["location"]
        self.money = kwargs["money"]
        self.car = Car(**kwargs["car"])

    def trip_cost(self, shop: Shop, fuel_price: float | int) -> float | int:
        total_cost = 2 * (self.car.fuel_consumption / 100 *
                          dist(self.location, shop.location) *
                          fuel_price)

        for name, count in self.product_cart.items():
            total_cost += count * shop.products[name]

        return round(total_cost, 2)
