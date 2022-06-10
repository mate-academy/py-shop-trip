import json
import datetime
from pathlib import Path
from decimal import Decimal
from dataclasses import dataclass

from app.shops import shops


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict

    def get_trip_cost(self, shop):
        distance = sum(
            [(x - y) ** 2 for x, y in zip(
                shop.location,
                self.location
            )]) ** 0.5

        fuel_cost = round(
            distance * fuel_prise / 100 * self.car["fuel_consumption"] * 2,
            2)
        products_cost = sum(
            shop.products[product] * self.product_cart[product]
            for product in self.product_cart)
        trip_cost = Decimal(str(products_cost)) + Decimal(str(fuel_cost))
        return trip_cost

    def find_cheapest_shop(self):
        cheapest_trip = 0
        for shop in shops:
            trip_cost = self.get_trip_cost(shop)
            if cheapest_trip == 0 or cheapest_trip > trip_cost:
                cheapest_trip = trip_cost
                cheapest_shop = shop
            print(f"{self.name}'s trip "
                  f"to the {shop.name} "
                  f"costs {self.get_trip_cost(shop)}")
        return cheapest_shop, cheapest_trip

    def go_to_cheapest_shop(self, shop):
        print(f"{self.name} rides to {shop.name}\n")
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!\n"
              f"You have bought: ")
        products_cost = 0
        for product, amount in self.product_cart.items():
            product_cost = amount * shop.products[product]
            print(f"{amount} {product}s for {product_cost} dollars")
            products_cost += product_cost
        print(f"Total cost is {products_cost} dollars")
        print(f"See you again!\n")
        print(f"{self.name} rides home")


path = Path(__file__).resolve().parent
with open(path / "config.json", "r") as file:
    config = json.load(file)
    fuel_prise = config["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config["customers"]]
