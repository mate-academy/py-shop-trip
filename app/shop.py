from dataclasses import dataclass
import json
from app.customer import Customer
import math


@dataclass
class Shop:
    name: str
    location: list[int, int]
    products: dict

    fuel_price = 0

    @classmethod
    def from_dict(cls, data: dict) -> "Shop":
        return cls(
            name=data["name"],
            location=data["location"],
            products=data["products"]
        )

    def load_customers(self) -> list:
        with open("config.json", "r") as file:
            data = json.load(file)
            self.fuel_price = data["FUEL_PRICE"]
        return [Shop.from_dict(shop) for shop in data["shops"]]

    def calculate_cost_to_reach(self, customer: Customer) -> float:
        distance = math.sqrt(
            (self.location[0] - customer.location[0]) ** 2
            + (self.location[1] - customer.location[1]) ** 2)
        l_on_100 = self.fuel_price * customer.car.fuel_consumption
        money_for_the_road = (distance * l_on_100) / 100
        return money_for_the_road

    def money_for_products(self, customer: Customer) -> float:
        product = (
                customer.product_cart["milk"] * self.products["milk"]
                + customer.product_cart["bread"] * self.products["bread"]
                + customer.product_cart["butter"] * self.products["butter"]
        )
        return product

    def shopping_cost(self, customer: Customer) -> float:
        Shop.load_customers(self)
        cost_of_trip = self.calculate_cost_to_reach(customer) * 2
        cost_of_products = self.money_for_products(customer)
        return round((cost_of_products + cost_of_trip), 2)
