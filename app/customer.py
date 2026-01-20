from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: Decimal
    car: Car

    def calculate_shop_trip(self, shop: Any, fuel_price: float) -> Decimal:
        distance = Decimal(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        ).sqrt()
        spent_on_fuel = (
            Decimal(f"{fuel_price}")
            * Decimal(f"{self.car.fuel_consumption}")
            / 100
            * distance
            * 2
        )
        spent_on_products = Decimal(
            sum(
                [
                    Decimal(self.product_cart[product])
                    * Decimal(f"{shop.products[product]}")
                    for product in self.product_cart
                ]
            )
        )
        spent_total = spent_on_fuel + spent_on_products
        return spent_total

    def ride(self, shop: Any, price: Decimal) -> None:
        home = self.location
        self.location = shop.location
        shop.sell(self)
        self.location = home
        self.money = self.money - price
        print(
            f"{self.name} rides home\n{self.name} "
            f"now has {round(self.money, 2)} dollars\n"
        )
