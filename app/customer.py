import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = list(location)
        self.money = money
        self.car = car

    def distance_to(self, shop: Shop) -> float:
        return math.dist(self.location, shop.location)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        road_cost = self.car.fuel_cost(self.distance_to(shop), fuel_price)
        return round(
            road_cost * 2 + shop.products_cost(self.product_cart), 2
        )

    def make_trip(self, shop: Shop, cost: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        shop.print_receipt(self.name, self.product_cart)
        print(f"{self.name} rides home")
        self.location = self.home_location
        self.money = round(self.money - cost, 2)
        print(f"{self.name} now has {self.money} dollars\n")
