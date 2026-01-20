from typing import Dict, Tuple
from math import sqrt
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        location: Tuple[int, int],
        money: float,
        cart: Dict[str, int],
        car: Car
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.cart = cart
        self.car = car
        self.home = location

    def distance_to(self, target: Tuple[int, int]) -> float:
        return sqrt(
            (self.location[0] - target[0]) ** 2
            + (self.location[1] - target[1]) ** 2
        )

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_to_shop = self.car.fuel_cost(distance, fuel_price)
        fuel_home = self.car.fuel_cost(distance, fuel_price)
        products = shop.calculate_product_cost(self.cart)
        return round(fuel_to_shop + products + fuel_home, 2)

    def go_to(self, location: Tuple[int, int]) -> None:
        self.location = location

    def go_home(self) -> None:
        self.location = self.home
