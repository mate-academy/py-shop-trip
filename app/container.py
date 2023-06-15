from app.units.customer import Customer
from app.units.car import Car
from app.units.product_cart import ProductCart
from app.units.shop import Shop, Showcase
from app.units.location import Location
from os import path

import json


class Deserializer:
    def __init__(self) -> None:
        with open(path.join("app", "config.json"), "r") as f:
            data = json.load(f)
        self.fuel_price = data["FUEL_PRICE"]
        self.customers = [
            self.deserialize_customer(customer)
            for customer in data["customers"]
        ]
        self.shops = [
            self.deserialize_shop(shop)
            for shop in data["shops"]
        ]

    @staticmethod
    def deserialize_customer(customer: dict) -> Customer:
        name = customer["name"]
        product_cart = ProductCart(
            milk=customer["product_cart"]["milk"],
            butter=customer["product_cart"]["butter"],
            bread=customer["product_cart"]["bread"]
        )
        location = Location(
            x_axis=customer["location"][0],
            y_axis=customer["location"][1]
        )
        money = customer["money"]
        car = Car(
            brand=customer["car"]["brand"],
            fuel_consumption=customer["car"]["fuel_consumption"],
        )
        return Customer(
            name=name,
            product_cart=product_cart,
            location=location,
            money=money,
            car=car
        )

    @staticmethod
    def deserialize_shop(shop: dict) -> Shop:
        name = shop["name"]
        location = Location(
            x_axis=shop["location"][0],
            y_axis=shop["location"][1]
        )
        products = Showcase(
            milk=shop["products"]["milk"],
            butter=shop["products"]["butter"],
            bread=shop["products"]["bread"]
        )
        return Shop(name=name, location=location, products=products)


class TripProcessor(Deserializer):
    def process_users(self) -> None:
        for customer in self.customers:
            customer.print_info()
            customer.calculate_all_shops_trip(self.shops, self.fuel_price)
            customer.shop_trip()
