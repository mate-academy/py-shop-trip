from dataclasses import dataclass
from math import dist

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: float
    car: Car

    def count_total_price(self, shop: Shop) -> float:
        result = 0
        for product in self.product_cart:
            result += self.product_cart[product] * shop.products[product]
        result += self.car.full_price * dist(shop.location, self.location) * 2
        return result
