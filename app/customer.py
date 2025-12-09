from __future__ import annotations
import math

from typing import TYPE_CHECKING
from app.car import Car

if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location.copy()
        self.money = money
        self.car = car

    def count_distance(self, shop: Shop) -> float:
        difference_x = shop.location[0] - self.location[0]
        difference_y = shop.location[1] - self.location[1]
        squared_distance = (difference_x ** 2) + (difference_y ** 2)
        distance_to_shop = math.sqrt(squared_distance)

        return distance_to_shop

    def calculate_fuel_cost(
            self,
            distance: int | float,
            fuel_price: int | float
    ) -> int | float:
        fuel_to_ride = (distance * self.car.fuel_consumption) / 100
        total_price = fuel_to_ride * fuel_price
        return total_price

    def has_all_products(self, shop: Shop) -> bool:
        products_to_buy = set(self.product_cart.keys())
        products_in_shop = set(shop.products.keys())

        return products_to_buy.issubset(products_in_shop)

    def calculate_products_cost(self, shop: Shop) -> int | float:
        return sum(
            shop.products[product] * count
            for product, count in self.product_cart.items()
        )

    def ride_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location

    def spend_money(self, amount: int | float) -> None:
        self.money -= amount

    def money_status(self) -> None:
        print(f"{self.name} has {self.money} dollars")
