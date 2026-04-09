import math
from app.car import Car
from typing import Any


class Customer:

    def __init__(self, name: str,
                 product_cart: dict,
                 location: list, money: int | float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def get_cart_cost(self, shop: Any) -> float:
        products_cost = 0
        for product, count in self.product_cart.items():
            if product not in shop.products:
                return float("inf")
            price = shop.products[product]
            products_cost += price * count

        return round(products_cost, 2)

    def calculate_trip_cost(self, shop: Any,
                            fuel_price: int | float) -> int | float:
        distance = self.get_distance(shop.location)

        fuel_needed = self.car.get_fuel_needed(distance * 2)
        fuel_cost = fuel_needed * fuel_price

        return fuel_cost + self.get_cart_cost(shop)

    def drive_to(self, new_location: list) -> None:
        self.location = new_location

    def buy_products(self, shop: Any) -> None:
        shop.print_receipt(self)

    def get_distance(self, target_location: list) -> float:
        x1, y1 = self.location
        x2, y2 = target_location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
