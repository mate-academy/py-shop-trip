from __future__ import annotations

import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data.get("name")
        self.product_cart: dict = customer_data.get("product_cart")
        self.location: list[int] = customer_data.get("location")
        self.money: float | int = customer_data.get("money")
        self.car: Car = Car(customer_data.get("car"))

    @staticmethod
    def calculate_distance(
            home_location: list[int],
            shop_location: list[int]
    ) -> float:
        return math.sqrt(
            (home_location[0] - shop_location[0]) ** 2
            + (home_location[1] - shop_location[1]) ** 2
        ) * 2

    def calculate_fuel_cost(
            self,
            fuel_price: float,
            shop_location: list[int]
    ) -> float:
        distance = self.calculate_distance(self.location, shop_location)
        return distance * self.car.fuel_consumption * fuel_price / 100

    def get_trip_price(
            self,
            fuel_price: float,
            shop_location: list,
            shop_products: dict
    ) -> float:
        fuel_cost = self.calculate_fuel_cost(fuel_price, shop_location)
        products_cost = sum(
            count * shop_products[product]
            for product, count in self.product_cart.items()
            if product in shop_products
        )

        return round(fuel_cost + products_cost, 2)

    def get_cheapest_shop(self, fuel_price: float, shops: list[Shop]) -> Shop:
        cheapest_shop = None
        min_trip_price = float("inf")

        for shop in shops:
            trip_price = self.get_trip_price(
                fuel_price,
                shop.location,
                shop.products
            )
            print(f"{self.name}'s trip to the {shop.name} costs {trip_price}")

            if trip_price < min_trip_price and self.money >= trip_price:
                min_trip_price = trip_price
                cheapest_shop = shop

        return cheapest_shop

    def ride_to_shop(self, fuel_price: float, shop: Shop) -> None:
        self.money -= self.get_trip_price(
            fuel_price,
            shop.location,
            shop.products
        )
        print(f"{self.name} rides to {shop.name}")
        print()
        shop.print_receipt(self.name, self.product_cart)
        print()
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")
        print()
