from __future__ import annotations
import dataclasses
import math
from typing import Dict, List


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: Dict
    location: List[int]
    money: int
    car: Dict
    enough_money: bool = False
    home_location = None

    def calculate_products_cost(self, products: dict) -> float:
        return sum(
            self.product_cart[product] * products[product]
            for product in self.product_cart
        )

    def calculate_fuel_cost(self, other: Shop, fuel_price) -> float:
        distance = math.sqrt(
            pow((other.location[0] - self.location[0]), 2)
            + pow((other.location[1] - self.location[1]), 2)
        )
        return fuel_price * self.car["fuel_consumption"] * distance / 100 * 2

    def pick_cheapest_trip(self, shops: List[Shop], fuel_price: float) -> tuple:
        trips_cost = dict()
        for shop in shops:
            products_cost = self.calculate_products_cost(shop.products)
            fuel_cost = self.calculate_fuel_cost(shop, fuel_price)
            trip_cost = round(products_cost + fuel_cost, 2)
            print(
                f"{self.name}'s trip to the {shop.name} Shop costs {trip_cost}"
            )
            trips_cost.update({shop: trip_cost})
        target_shop = min(trips_cost, key=trips_cost.get)
        return target_shop, trips_cost[target_shop]

    def drives_to_shop(self, shop: Shop) -> None:
        self.home_location = list(self.location)
        print(f"{self.name} rides to {shop.name} Shop\n")
        self.location = shop.location
        shop.print_receipt(self)

    def drives_home(self, trip_cost: float) -> None:
        print(f"{self.name} rides home.")
        self.location = self.home_location
        self.money -= trip_cost
        print(f"{self.name} now has {self.money} dollars\n")


@dataclasses.dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict

    def print_receipt(self, customer: Customer) -> None:
        print(
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: \n"
        )
        total_cost = 0
        for product in customer.product_cart:
            quantity = customer.product_cart[product]
            cost = quantity * self.products[product]
            total_cost += cost
            product_name = product
            currency = "dollar"
            if quantity > 1:
                product_name = f"{product_name}s"
            if cost > 1:
                currency = f"{currency}s"
            print(f"{quantity} {product_name} for {cost} {currency}\n")
        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
