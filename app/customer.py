import math

from app.car import Car
from app.shop import Shop
from app.utils import format_money


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car_data: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = location.copy()
        self.current_location = location.copy()
        self.money = money
        self.car = Car(**car_data)

    def calculate_distance(self, target_location: list) -> float:
        return math.dist(self.current_location, target_location)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)

        fuel_needed = (distance * 2 / 100) * self.car.fuel_consumption
        fuel_cost = fuel_needed * fuel_price

        products_cost = shop.calculate_products_cost(self.product_cart)

        return fuel_cost + products_cost

    def perform_trip(self, shop: Shop, total_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.current_location = shop.location.copy()

        shop.print_receipt(self.name, self.product_cart)

        print(f"{self.name} rides home")
        self.current_location = self.home_location.copy()

        self.money -= total_cost

        print(f"{self.name} now has {format_money(self.money)} dollars")
