import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int | float],
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(
            self.location,
            shop.location
        )
        fuel_cost = (
            distance * self.car.fuel_consumption * 0.01 * fuel_price * 2
        )
        products_cost = sum([
            amount * shop.products[product]
            for product, amount in self.product_cart.items()
        ])
        return round(fuel_cost + products_cost, 2)
