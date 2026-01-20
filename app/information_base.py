import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def create_lists_customers_shops() -> tuple:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "config.json")
    with open(path, "r") as config_file:
        config = json.load(config_file)
    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        ) for shop in config["shops"]
    ]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        ) for customer in config["customers"]
    ]
    return fuel_price, customers, shops
