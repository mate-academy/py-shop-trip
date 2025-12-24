from __future__ import annotations
from app.shop import Shop
from app.car import Car
from math import sqrt


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: int, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location.copy()

    def distance_to(self, destination: list) -> float:
        return sqrt((self.location[0] - destination[0]) ** 2
                    + (self.location[1] - destination[1]) ** 2)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = self.distance_to(shop.location)
        fuel_cost = self.car.fuel_cost(distance_to_shop * 2, fuel_price)
        products_cost = shop.calculate_cart_price(self.product_cart)
        return round(fuel_cost + products_cost, 2)

    def ride_to(self, location: list) -> None:
        self.location = location

    def ride_home(self) -> None:
        self.location = self.home_location
