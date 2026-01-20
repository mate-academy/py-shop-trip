import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(self, shop: Shop) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_cost = (distance / 100) * self.car.fuel_consumption * shop.fuel
        product_cost = self.calculate_product_cost(shop)
        total_cost = fuel_cost + product_cost + fuel_cost
        return round(total_cost, 2)

    def calculate_distance(self, shop_location: list) -> float:
        return math.dist(self.location, shop_location)

    def calculate_product_cost(self, shop: Shop) -> float:
        return sum(
            shop.products[product] * quantity
            for product, quantity in self.product_cart.items()
            if product in shop.products
        )
