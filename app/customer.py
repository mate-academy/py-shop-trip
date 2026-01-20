from __future__ import annotations

import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.location = location
        self.product_cart = product_cart
        self.money = money
        self.car = car

    def find_full_cost_of_travel(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> dict[Shop, int | float]:
        result = {}
        for shop in shops:
            travel_distance_cost = self.car.calculate_cost_of_trip(
                self.location,
                shop.location,
                fuel_price
            ) * 2
            products_cost = shop.get_price_of_product_cart(self.product_cart)
            full_cost = travel_distance_cost + products_cost
            result[shop] = full_cost
        return result

    def print_customer_purchase(self, suitable_shop: Shop) -> None:
        print(f"{self.name} rides to {suitable_shop.name}\n")
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, count in self.product_cart.items():
            product_cost = suitable_shop.products[product] * count
            if product_cost - int(product_cost) == 0:
                product_cost = int(product_cost)
            total_cost += product_cost
            print(f"{count} {product}s for {product_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print(f"See you again!\n\n{self.name} rides home")

    def find_cheapest_trip(
            self,
            trip_to_shop_costs: dict[Shop, float]
    ) -> tuple[Shop, float]:
        suitable_shop, price = None, float("inf")
        for shop, trip_price in trip_to_shop_costs.items():
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {round(trip_price, 2)}")
            if trip_price < price:
                suitable_shop, price = shop, trip_price
        return suitable_shop, price

    @staticmethod
    def json_list_to_customer_objects(
            customers: list[dict]
    ) -> list[Customer]:
        return [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                ),
            )
            for customer in customers
        ]
