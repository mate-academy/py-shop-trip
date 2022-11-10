from copy import copy

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, datasource: dict) -> None:
        self.name = datasource["name"]
        self.product_cart = datasource["product_cart"]
        self.location = datasource["location"]
        self.money = datasource["money"]
        self.car = datasource["car"]
        self.home_location = datasource["location"]

    def cost_trip_to(self, shop: Shop) -> float:
        car = Car(self.car["brand"], self.car["fuel_consumption"])
        return car.cost_trip(self.location, shop.location)

    def cost_purchase_product(self, shop: Shop) -> float:
        cost = 0
        for product_name, number in self.product_cart.items():
            cost += shop.products[product_name] * number
        return cost

    def ride_to(self, shop: Shop) -> None:
        self.location = copy(shop.location)
        print(f"{self.name} rides to {shop.name}\n")

    def rides_home(self) -> None:
        self.location = copy(self.home_location)
        print(f"{self.name} rides home")
