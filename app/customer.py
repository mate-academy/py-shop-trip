from typing import Any
from app.car import Car
import math

from app.utils import format_price


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = location.copy()

    def calculate_distance(self, other_location: list) -> float:
        x1, y1 = self.home
        x2, y2 = other_location
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def choose_shop(self, shops: list, fuel_price: float) -> Any:
        best_shop = None
        lowest_total = float("inf")

        for shop in shops:
            if not all(product in shop.products
                       for product in self.product_cart):
                continue

            distance = self.calculate_distance(shop.location)
            fuel_cost = self.car.get_fuel_cost(distance * 2, fuel_price)

            product_cost = sum(shop.products[p] * a
                               for p, a in self.product_cart.items())
            total_cost = round(fuel_cost + product_cost, 2)

            print(f"{self.name}'s trip to the {shop.name}"
                  f" costs {format_price(total_cost)}")

            if total_cost <= self.money and total_cost < lowest_total:
                lowest_total = total_cost
                best_shop = shop

        if best_shop:
            return best_shop, lowest_total
        else:
            return None, None
