from dataclasses import dataclass
from app.car import Car
from app.shop import Shop
import math


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def distance_to(self, shop: Shop) -> float:
        return math.sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop)
        fuel_cost = self.car.fuel_cost(distance * 2, fuel_price)
        product_cost = shop.cart_cost(self.product_cart)
        total_cost = fuel_cost + product_cost
        return round(total_cost, 2)
