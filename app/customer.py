import json
import math
import os
from copy import copy
from app.car import Car
from app.shop import Shop

current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.json")


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = copy(location)

    def price_for_trip(self, shop: Shop, fuel_price: float) -> float:
        distance = math.sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )
        fuel_cost = distance * self.car.price_for_km(fuel_price)
        products_cost = (shop.products["milk"] * self.product_cart["milk"]
                         + shop.products["bread"]
                         * self.product_cart["bread"]
                         + shop.products["butter"]
                         * self.product_cart["butter"])
        return round(fuel_cost * 2 + products_cost, 2)

    def define_cheapest(self, shops: list, fuel_price: float) -> Shop:
        shops_dict = {}
        for shop in shops:
            price = self.price_for_trip(shop, fuel_price)
            shops_dict[shop.name] = price
        sorted_shops = dict(
            sorted(shops_dict.items(), key=lambda item: item[1])
        )
        cheapest = list(sorted_shops.keys())[0]
        for shop in shops:
            if shop.name == cheapest:
                return shop


def define_customers() -> list:
    with open(config_file_path, "r") as file:
        data = json.load(file)
        customers = []
        for customer in data["customers"]:
            customers.append(Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            ))
    return customers
