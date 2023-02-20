from __future__ import annotations

import math
from dataclasses import dataclass

from app.data import data
from app.car import Car
from app.customers import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    @staticmethod
    def create_shop() -> list[Shop]:
        shops_list = []
        for shop in data.get("shops"):
            shops_list.append(
                Shop(
                    name=shop.get("name"),
                    location=shop.get("location"),
                    products=shop.get("products")
                )
            )
        return shops_list

    def distance_cost(self, customer: Customer, car: Car) -> float:
        return round(
            math.dist(customer.location, self.location) * 2
            / 100 * car.fuel_price * customer.car.fuel_consumption_per_100_km,
            2
        )

    def product_costs(self, customer: Customer) -> float:
        product_costs = []
        for product in self.products:
            product_costs.append(self.products[product]
                                 * customer.product_cart[product])
        return sum(product_costs)

    def print_purchase(self, customer: Customer) -> None:
        for product, number in customer.product_cart.items():
            print(
                f"{number} {product}s for "
                f"{number * self.products[product]} dollars"
            )
