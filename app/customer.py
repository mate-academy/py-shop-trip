from app.car import Car
from app.shop import Shop
import math


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location.copy()
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        fuel_to_shop = self.car.calculate_fuel_cost(distance, fuel_price)
        fuel_to_home = self.car.calculate_fuel_cost(distance, fuel_price)
        products_cost = shop.calculate_products_cost(self.product_cart)
        return fuel_to_shop + fuel_to_home + products_cost

    def visit_shop(self, shop: Shop, fuel_price: float) -> None:
        total_cost = self.calculate_trip_cost(shop, fuel_price)

        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

        shop.print_receipt(self.name, self.product_cart)

        print(f"{self.name} rides home")

        self.money -= total_cost
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")
