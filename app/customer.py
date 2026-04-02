import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: float,
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car) if isinstance(car, dict) else car

    def distance_to(self, shop: Shop) -> float:
        return math.dist(self.location, shop.location)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop)

        fuel_cost = self.car.fuel_cost(distance, fuel_price) * 2
        products_cost = shop.calculate_products_cost(self.product_cart)

        return fuel_cost + products_cost

    def go_to_shop(self, shop: Shop) -> None:
        self.location = shop.location

    def go_home(self, home_location: float) -> None:
        self.location = home_location
