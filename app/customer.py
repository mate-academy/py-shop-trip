import math
from dataclasses import dataclass
from typing import Any

from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    @staticmethod
    def read_customer_json(data: list) -> list:
        return [Customer(**customer) for customer in data]

    def cost_for_trip_to_the_shop(self, shop: Shop, fuel_price: Any) -> float:
        distance_x = (self.location[0] - shop.location[0]) ** 2
        distance_y = (self.location[1] - shop.location[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        one_way_trip = distance * fuel_price * self.car["fuel_consumption"]
        trip_cost = round(((one_way_trip / 100) * 2), 2)
        return trip_cost

    def product_cost(self, shop: Shop) -> float:
        product_cost = 0
        for product, quantity in self.product_cart.items():
            product_cost += shop.products[product] * quantity
        return product_cost
