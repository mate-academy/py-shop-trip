from app.car import Car
from app.shop import Shop

import math


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def get_distance(self, shop_location: list) -> float:
        return math.hypot(
            shop_location[0] - self.location[0],
            shop_location[1] - self.location[1]
        )

    def get_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.get_distance(shop.location)
        total_fuel_cost = self.car.get_fuel_cost(distance, fuel_price)
        total_products_cost = shop.get_product_cost(self.product_cart)
        return total_fuel_cost + total_products_cost

    def go_to_shop(self, shop: Shop, fuel_price: float) -> None:
        print(f"{self.name} rides to {shop.name}")
        home = self.location
        distance = self.get_distance(shop.location)
        road_cost = self.car.get_fuel_cost(distance, fuel_price)
        products_cost = shop.get_product_cost(self.product_cart)

        self.money -= (road_cost + products_cost)
        self.location = shop.location

        print()
        shop.print_recipe(self.name, self.product_cart)
        print()

        self.location = home
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars")
