from __future__ import annotations
from dataclasses import dataclass
from math import sqrt
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:

    name: str
    product_cart: dict
    location: list[int]
    money: int | float
    car: Car

    def calculate_distance(self, shop: Shop) -> int | float:
        x1, y1 = (self.location[0], self.location[1])
        x2, y2 = (shop.location[0], shop.location[1])

        return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    def calculate_travel_cost(
        self,
        fuel_price: float,
        shop: Shop
    ) -> int | float:

        l_per_km = self.car.fuel_consumption / 100
        distance = self.calculate_distance(shop)
        return round(l_per_km * distance * fuel_price * 2, 2)

    def calculate_cart_cost(self, shop: Shop) -> int | float:
        if shop.products:
            cart_cost = 0
            for item in self.product_cart:
                cart_cost += self.product_cart[item] * shop.products[item]
            return cart_cost
        return 0

    def calculate_total_cost(
        self,
        fuel_price: float,
        shop: Shop
    ) -> int | float:
        travel_cost = self.calculate_travel_cost(fuel_price, shop)
        cart_cost = self.calculate_cart_cost(shop)
        return travel_cost + cart_cost
