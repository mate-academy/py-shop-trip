from typing import Dict
from app.shop import Shop


class Customer:
    def __init__(self, data: Dict[str, Dict], fuel_price: float) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = data["car"]
        self.fuel_price = fuel_price

    def calculate_price_of_trip(self, shop: object, car: object, fuel_price: float) -> int:
        price_trip = 0
        for product, amount in self.product_cart.items():
            price_trip += shop.calculate_product(product, amount)
        price_trip += car.calculate_price_of_way(shop.location[0],
                                                 shop.location[1], fuel_price)
        return price_trip

    def go_shopping(self, shops: list, car: object) -> None:
        print(f"{self.name} has {self.money} dollars")

        cheapest_trip: Dict[str, float | Shop] = {
            "cost": 0.0,
            "shop": None
        }

        for shop in shops:
            trip_and_shopping_cost = self.calculate_price_of_trip(
                shop, car, self.fuel_price
            )

            print(
                f"{self.name}'s trip to the {shop.name}"
                f" costs {round(trip_and_shopping_cost, 2)}"
            )

            if (
                    trip_and_shopping_cost <= self.money
                    and (
                    trip_and_shopping_cost
                    < cheapest_trip["cost"]
                    or cheapest_trip["shop"] is None
            )
            ):
                cheapest_trip = {
                    "cost": trip_and_shopping_cost,
                    "shop": shop
                }

        if cheapest_trip["shop"] is None:
            print(
                f"{self.name} doesn't have enough money"
                " to make purchase in any shop"
            )
            return

        print(f"{self.name} rides to {cheapest_trip['shop'].name}")

        shop.buy_products(self.name, self.product_cart)

        self.money -= cheapest_trip["cost"]
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - cheapest_trip['cost']} dollars")
