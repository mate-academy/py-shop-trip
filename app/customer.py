from typing import Dict, List
from math import dist

from app.shop import Shop


class Customer:
    def __init__(
        self,
        data: Dict[str, Dict],
        fuel_price: float
    ) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = data["car"]
        self.fuel_price = fuel_price

    def go_shoping(self, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")

        cheapest_trip: Dict[str, float | Shop] = {
            "cost": 0.0,
            "shop": None
        }

        for shop in shops:
            trip_and_shoping_cost = self.calculate_cost_of_trip_and_shoping(
                shop
            )

            print(
                f"{self.name}'s trip to the {shop.name}"
                f" costs {round(trip_and_shoping_cost, 2)}"
            )

            if (
                trip_and_shoping_cost <= self.money
                and (
                    trip_and_shoping_cost
                    < cheapest_trip["cost"]
                    or cheapest_trip["shop"] is None
                )
            ):
                cheapest_trip = {
                    "cost": trip_and_shoping_cost,
                    "shop": shop
                }

        if cheapest_trip["shop"] is None:
            print(
                f"{self.name} doesn't have enough money"
                " to make purchase in any shop"
            )
            return

        self.ride_to_shop(cheapest_trip["shop"])

        self.money -= cheapest_trip["shop"].buy_products(
            self.name,
            self.product_cart
        )

        self.ride_to_home(cheapest_trip["shop"])

    def ride_to_home(self, shop: Shop) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location
        self.money -= self.cost_of_trip(shop)
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

    def ride_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.money -= self.cost_of_trip(shop)
        self.home_location = self.location
        self.location = shop.location

    def calculate_cost_of_trip_and_shoping(
        self,
        shop: Shop
    ) -> float:
        return 2 * self.cost_of_trip(shop) + self.cost_of_shoping(shop)

    def cost_of_trip(self, shop: Shop) -> float:
        distance_to_shop = dist(self.location, shop.location)

        return (
            distance_to_shop
            * self.car["fuel_consumption"]
            / 100
            * self.fuel_price
        )

    def cost_of_shoping(self, shop: Shop) -> float:
        cost_of_products = 0

        for product, amount in self.product_cart.items():
            cost_of_products += (
                shop.get_product_price(product, amount)
            )

        return cost_of_products
