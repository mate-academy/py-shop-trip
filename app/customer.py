import math
from typing import Dict, Any, Union
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: Dict[str, int],
                 location: list[int], money:
                 Union[int, float],
                 car: Dict[str, Any]) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = float(money)
        self.car = Car(car["brand"], float(car["fuel_consumption"]))

    def get_distance_to(self, shop: Shop) -> float:
        return float(math.dist(self.location, shop.location))

    def evaluate_trip(self, shop: Shop, fuel_price: float) -> float:
        distance = self.get_distance_to(shop)
        fuel_to_shop = self.car.get_fuel_cost(distance, fuel_price)
        fuel_to_home = self.car.get_fuel_cost(distance, fuel_price)

        products_cost = shop.get_cart_cost(self.product_cart)
        return products_cost + fuel_to_shop + fuel_to_home

    def ride_to_shop(self, shop: Shop) -> None:
        self.location = list(shop.location)
