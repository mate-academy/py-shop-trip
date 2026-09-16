import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self, name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location.copy()
        self.money = money
        self.car = car

    def calculate_distance(self, location: list[int]) -> float:
        x1, y1 = self.location
        x2, y2 = location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance * 2, fuel_price)
        products_cost = shop.calculate_products_cost(self.product_cart)
        return fuel_cost + products_cost

    def go_to_shop(self, shop: Shop) -> None:
        self.location = shop.location

    def buy_products(self, shop: Shop) -> float:
        products_cost = shop.calculate_products_cost(
            self.product_cart
        )
        self.money -= products_cost
        return products_cost

    def go_home(self) -> None:
        self.location = self.home_location
