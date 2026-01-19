import json
import os
from typing import Any

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_data() -> list[Any]:
    abs_path = os.path.join(os.getcwd(), "app", "config.json")

    with open(abs_path, "r") as data_file:
        data = json.load(data_file)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        )
        for customer in data["customers"]
    ]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]

    return [fuel_price, customers, shops]
