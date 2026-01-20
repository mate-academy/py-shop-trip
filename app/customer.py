from __future__ import annotations

import json
from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


class InsufficientFundsException(Exception):
    pass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: Car

    def print_balance(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def choose_shop_to_visit(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> Shop | None:

        lowest_price = None

        for shop in shops:
            ride_cost = self.car.calculate_trip_cost(
                self.location, shop.location, fuel_price
            )
            ride_cost *= 2
            trip_cost = ride_cost + shop.calculate_cart_cost(self.product_cart)

            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")

            if lowest_price is None or trip_cost < lowest_price:
                lowest_price = trip_cost
                shop_to_visit = shop

        if lowest_price is not None and lowest_price <= self.money:
            print(f"{self.name} rides to {shop_to_visit.name}\n")
            self.money -= lowest_price
            return shop_to_visit

        print(f"{self.name} doesn't have enough money "
              f"to make a purchase in any shop")
        return None

    def make_purchase(self, shop: Shop) -> float:
        total = shop.calculate_cart_cost(self.product_cart)

        if total >= self.money:
            raise InsufficientFundsException

        return total

    def buy_products(self, shop: Shop) -> None:
        try:
            self.make_purchase(shop)
            shop.get_receipt(self.name, self.product_cart)

        except InsufficientFundsException:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in {shop.name}")

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")


def load_customers_from_json(file_name: str) -> list[Customer]:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        customers = data["customers"]
        return [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )
            for customer in customers
        ]
