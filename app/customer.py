from typing import Dict, List

from app.car import Car
from app.shop import Shop
from app.utils import distance


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: Dict[str, int],
        location: List[float],
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = location[:]

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = distance(self.location, shop.location)
        fuel = self.car.fuel_cost(dist * 2, fuel_price)
        products = shop.products_cost(self.product_cart)
        return fuel + products

    def can_afford(self, cost: float) -> bool:
        return self.money >= cost
