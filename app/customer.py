import math

from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_total_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = self.calculate_distance(shop)
        total_fuel_cost = self.car.trip_cost(distance_to_shop * 2, fuel_price)
        products_cost = shop.total_cost_of_products(self.product_cart)
        return round(total_fuel_cost + products_cost, 2)

    @staticmethod
    def moving_to_shop(shop: Shop) -> list:
        return shop.location

    def moving_home(self) -> list:
        return self.location
