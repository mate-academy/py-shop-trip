from __future__ import annotations
import json
import math
from typing import Any

from app.car import Car


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
        self.money = money
        self.car = car

    @classmethod
    def from_dict(cls, customer_data: dict, car: Car) -> Customer:
        new_customer = cls(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car,
        )
        return new_customer

    def calculate_fuel_cost(
        self, destination: list, fuel_cost: float
    ) -> float:
        x1, y1 = self.location
        x2, y2 = destination
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        fuel_needed = (distance / 100) * self.car.fuel_consumption
        total_fuel_cost = fuel_needed * fuel_cost * 2
        return total_fuel_cost

    def find_the_cheapest_shop(self, shops: list, fuel_cost: float) -> tuple:
        cheapest_total = 0
        shop_to_go = None
        for shop in shops:
            cost_of_fuel = self.calculate_fuel_cost(shop.location, fuel_cost)
            cost_of_products = shop.calculate_cart(self.product_cart)
            full_cost = round(cost_of_products + cost_of_fuel, 2)

            if not cheapest_total or full_cost < cheapest_total:
                cheapest_total = full_cost
                shop_to_go = shop

            print(f"{self.name}'s trip to the {shop.name} costs {full_cost}")

        return shop_to_go, cheapest_total

    def ride_to_shop(self, shop: Any) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

    def ride_to_home(self, home: list) -> None:
        print(f"{self.name} rides home")
        self.location = home

    def count_money_after_shop(self, total_cost: int) -> None:
        self.money -= total_cost
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")


def load_customers(file_data: json) -> list:
    return [
        Customer.from_dict(customer_data, car=Car(**customer_data["car"]))
        for customer_data in file_data["customers"]
    ]
