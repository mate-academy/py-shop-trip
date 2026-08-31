import json
import os
from typing import Any

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def initialisation(filename: str) -> Any:
    config_path = os.path.join(os.path.dirname(__file__), filename)
    with open(config_path) as f:
        data = json.load(f)

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
    return fuel_price, customers, shops
