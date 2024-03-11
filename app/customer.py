import json
import math
from dataclasses import dataclass
from app.car import fuel_price
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def distance(self, shop: Shop) -> float:
        pow_x_coordinate = pow(self.location[0] - shop.location[0], 2)
        pow_y_coordinate = pow(self.location[1] - shop.location[1], 2)
        return math.sqrt(pow_x_coordinate + pow_y_coordinate)

    def product_value(self, shop: Shop) -> float:
        return sum(
            self.product_cart[product_name] * shop.products[product_name]
            for product_name in self.product_cart
        )

    def price_trip(self, shop: Shop) -> float:
        fuel_consumption = self.car["fuel_consumption"]
        distance = self.distance(shop)
        price_road = 2 * (fuel_consumption / 100) * distance * fuel_price
        price_product = self.product_value(shop)

        return round(price_road + price_product, 2)


with open("app/config.json", "r") as file:
    customers = json.load(file)["customers"]

customers_list = [
    Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"],
        car=customer["car"]
    )
    for customer in customers
]
