import math
from typing import TYPE_CHECKING

from app.car import Car

if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop_location: list[int]) -> float:
        return math.dist(self.location, shop_location)

    def calculate_trip_cost(self, shop: "Shop", fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance * 2, fuel_price)
        return fuel_cost + shop.calculate_products_cost(self.product_cart)

    def can_afford(self, trip_cost: float) -> bool:
        return self.money >= trip_cost

    def ride_to(self, location: list[int]) -> None:
        self.location = location.copy()

    def spend_money(self, amount: float) -> None:
        self.money -= amount
