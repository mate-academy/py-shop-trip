import datetime
import math
from typing import Dict, Any, List

from app.car import Car


class Customer:

    def __init__(self, data: Dict[str, Any]) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"])

    def calculate_trip_cost(self, shop: "Shop") -> float:
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_consumption_per_km = self.car.fuel_consumption / 100
        fuel_cost_to_shop = (
            distance_to_shop * fuel_consumption_per_km
        ) * Car.FUEL_PRICE
        product_cost = sum(
            [
                self.product_cart[product] * shop.products[product]
                for product in self.product_cart
            ]
        )
        total_trip_cost = fuel_cost_to_shop + product_cost
        return round(total_trip_cost, 2)

    def has_enough_money(self, trip_cost: float) -> bool:
        return self.money >= trip_cost

    def travel_to_shop(self, shop: "Shop") -> None:
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def travel_home(self, trip_cost: float) -> None:
        print(f"{self.name} rides home\n")
        remaining_money = self.money - trip_cost
        print(f"{self.name} now has {round(remaining_money, 2)} dollars\n")

    def calculate_distance(self, shop_location: List[int]) -> float:
        x_location = self.location[0] - shop_location[0]
        y_location = self.location[1] - shop_location[1]
        distance = math.sqrt(x_location**2 + y_location**2)
        return distance


class Shop:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def sell_products(self, customer: Customer) -> None:
        print(
            f"\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        )
        print(f"Thanks, {customer.name}, for your purchase!\n")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            product_cost = quantity * self.products[product]
            print(
                f"You have bought: {quantity} {product}s "
                f"for {product_cost} dollars\n"
            )
            total_cost += product_cost
        print(f"Total cost is {total_cost} dollars\n")
        print("See you again!\n")
