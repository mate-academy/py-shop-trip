import json
from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    customer_list = list()

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.customer_list.append(self)

    @staticmethod
    def create_from_dict(customers: dict) -> None:
        for customer in customers:
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

    def cost_of_the_trip(self, shop: Shop) -> float:
        with open("app/config.json", "r") as file:
            json_info = json.load(file)
        fuel_price = json_info["FUEL_PRICE"]

        products_cost = shop.cost_of_all_products(self.product_cart)
        return round((self.car.fuel_consumption / 100)
                     * (dist(self.location, shop.location) * 2)
                     * fuel_price, 2) + products_cost
