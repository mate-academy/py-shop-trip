import math
from typing import Any


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = tuple(data["location"])
        self.money = data["money"]
        self.car = None

    def distance_km(self, shop: Any) -> float:
        return math.hypot(self.location[0] - shop.location[0],
                          self.location[1] - shop.location[1])

    def calc_trip_cost(self, shop: Any, fuel_price: float) -> float:
        distance = self.distance_km(shop)
        fuel_one_way = self.car.calc_fuel_cost(distance, fuel_price)
        products_cost = shop.total_products_cost(self.product_cart)
        return fuel_one_way * 2 + products_cost
