from typing import Dict, List
from app.shop import Shop
from app.car import Car


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

    def calculate_price_of_trip(
            self,
            shop: Shop,
            car: Car,
            fuel_price: float
    ) -> int:
        price_trip = 0
        for product, amount in self.product_cart.items():
            price_trip += shop.calculate_product(product, amount)
        price_trip += car.calculate_price_of_way(shop.location[0],
                                                 shop.location[1], fuel_price)
        return round(price_trip, 2)

    def go_shopping(
            self,
            shops: List[Shop],
            car: Car
    ) -> None:
        print(f"{self.name} has {self.money} dollars")

        cheapest_trip = self.found_cheapest_trip(shops, car)

        if cheapest_trip["shop"] is None:
            print(
                f"{self.name} doesn't have enough money"
                " to make purchase in any shop"
            )
            return

        print(f"{self.name} rides to {cheapest_trip['shop'].name}\n")

        cheapest_trip["shop"].buy_products(self.name, self.product_cart)

        self.money -= cheapest_trip["cost"]
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def found_cheapest_trip(
            self,
            shops: List[Shop],
            car: Car
    ) -> Dict:
        cheapest_trip: Dict[str, float | Shop] = {
            "cost": 0.0,
            "shop": None
        }

        for shop in shops:
            trip_and_shopping_cost = round(self.calculate_price_of_trip(
                shop, car, self.fuel_price
            ), 2)

            print(
                f"{self.name}'s trip to the {shop.name}"
                f" costs {round(trip_and_shopping_cost, 2)}"
            )

            if (
                    trip_and_shopping_cost <= self.money
                    and (
                    trip_and_shopping_cost
                    < cheapest_trip["cost"]
                    or cheapest_trip["shop"] is None)
            ):
                cheapest_trip = {
                    "cost": trip_and_shopping_cost,
                    "shop": shop
                }

        return cheapest_trip
