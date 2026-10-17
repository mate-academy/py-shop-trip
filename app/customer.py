from __future__ import annotations
from app.car import Car
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
            self, name: str,
            product_cart: dict,
            location: tuple,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = tuple(location)
        self.money = money
        self.car = car

    def distance_to_shop(self, shop: "Shop") -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def total_price(self, shop: "Shop", fuel_price: float) -> float:
        total_distance_to_shop = self.distance_to_shop(shop) * 2
        fuel_cost = self.car.calculate_fuel_cost(
            total_distance_to_shop, fuel_price
        )
        total_price_of_products = 0.0
        for key, value in self.product_cart.items():
            price = shop.products[key] * value
            total_price_of_products += price
        return round(total_price_of_products + fuel_cost, 2)
