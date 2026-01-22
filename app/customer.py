from typing import Dict, List
from math import dist
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self, name: str,
            product_cart: Dict[str, int],
            location: List[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location[:]
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = dist(self.location, shop.location)
        distance_home = dist(shop.location, self.home_location)

        cost_to_shop = self.car.fuel_cost(distance_to_shop, fuel_price)
        cost_home = self.car.fuel_cost(distance_home, fuel_price)

        return round(cost_to_shop + cost_home, 2)

    def can_afford(self, cost: float) -> bool:
        return self.money >= cost

    def travel_to(self, location: List[int]) -> None:
        self.location = location

    def pay(self, amount: float) -> None:
        self.money = round(self.money - amount, 2)
