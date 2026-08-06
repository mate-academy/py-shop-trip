import math
from collections.abc import Callable

from app.car import Car


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list, money: int,
                 car_data: Callable) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car_data["brand"], car_data["fuel_consumption"])

    def get_distance_to(self, shop: str) -> float:
        return math.dist(self.location, shop.location)

    def evaluate_trip(self, shop: str, fuel_price: int) -> float:
        distance = self.get_distance_to(shop)
        fuel_cost = self.car.get_fuel_cost(distance, fuel_price)
        products_cost = shop.get_cart_cost(self.product_cart)
        return round(products_cost + fuel_cost, 2)
