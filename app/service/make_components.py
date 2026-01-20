import json
import os

from app.classes.customer import Customer
from app.classes.shop import Shop
from app.classes.car import Car

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
parent_dir = os.path.dirname(current_dir)

config_path = os.path.join(parent_dir, "config.json")


with open(config_path, "r") as config:
    config = json.load(config)


FUEL_PRICE = config.get("FUEL_PRICE")
customers = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
    ) for customer in config.get("customers")
]
shops = [
    Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    ) for shop in config.get("shops")
]
