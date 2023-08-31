import json
import os
from os.path import dirname
from app.car import Car
from app.customer import Customer

from app.shop import Shop

BASE_DIR: str = dirname(dirname(__file__))


def shop_trip() -> None:
    with open(os.path.join(BASE_DIR, "app", "config.json"), "r") as fobj:
        config: dict = json.load(fobj)

    fuel_price: float = config["FUEL_PRICE"]
    shops: list[Shop] = [Shop(**shop_dict) for shop_dict in config["shops"]]

    for i, customer_dict in enumerate(config["customers"]):
        car: Car = Car(**customer_dict["car"])
        customer: Customer = Customer(
            customer_dict["name"],
            customer_dict["product_cart"],
            customer_dict["location"],
            customer_dict["money"],
            car,
            fuel_price,
        )
        if i != 0:
            print()
        customer.make_purchase(shops)


shop_trip()
