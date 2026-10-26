from typing import Any

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[float],
        money: float,
        car: dict[str, Any],
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location[:]
        self.money = money
        self.car = Car(**car)
        self.fuel_price = 0.0

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        product_cost = shop.purchase_cost(self.product_cart)
        if product_cost is None:
            return float("inf")

        distance = self.car.distance(self.location, shop.location)
        fuel_cost = self.car.fuel_cost(distance, fuel_price)
        return product_cost + fuel_cost * 2

    def go_to(self, shop: Shop, fuel_price: float) -> None:
        distance = self.car.distance(self.location, shop.location)
        self.money -= self.car.fuel_cost(distance, fuel_price)
        self.fuel_price = fuel_price
        self.location = shop.location[:]

    def go_home(self) -> None:
        distance = self.car.distance(self.location, self.home_location)
        self.money -= self.car.fuel_cost(distance, self.fuel_price)
        self.location = self.home_location[:]
