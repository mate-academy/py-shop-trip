from __future__ import annotations
import math
import datetime
from typing import Dict, List


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str: int],
            location: List[int],
            money: int,
            car: Dict[str: int]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = tuple(location)
        self.money = money
        self.car = car
        self.enough_money = False
        self.home_location = tuple(self.location)

    def calculate_products_cost(self, products: Dict[str: int]) -> float:
        return sum(
            self.product_cart[product] * products[product]
            for product in self.product_cart
        )

    def calculate_fuel_cost(self, other: Shop, fuel_price: float) -> float:
        distance = math.sqrt(
            pow((other.location[0] - self.location[0]), 2)
            + pow((other.location[1] - self.location[1]), 2)
        )
        return fuel_price * self.car["fuel_consumption"] * distance / 100 * 2

    def pick_cheapest_trip(
            self,
            shops: List[Shop],
            fuel_price: float
    ) -> tuple:
        trips_cost = dict()
        for shop in shops:
            products_cost = self.calculate_products_cost(shop.products)
            fuel_cost = round(self.calculate_fuel_cost(shop, fuel_price), 2)
            trip_cost = products_cost + fuel_cost
            print(
                f"{self.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            trips_cost.update({shop: trip_cost})
        target_shop = min(trips_cost, key=trips_cost.get)
        return target_shop, trips_cost[target_shop]

    def drives_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        shop.print_receipt(self)

    def drives_home(self, trip_cost: float) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location
        self.money -= trip_cost
        print(f"{self.name} now has {self.money} dollars\n")


class Shop:
    def __init__(
        self,
        name: str,
        location: List[int],
        products: Dict[str: int]
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = products

    def print_receipt(self, customer: Customer) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"Date: {now}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
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
            print(f"{quantity} {product_name} for {cost} {currency}")
        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
