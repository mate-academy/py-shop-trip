import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            Car(**customer_data["car"]),
        )
        for customer_data in config["customers"]
    ]
    shops = [Shop(**shop_data) for shop_data in config["shops"]]

    for index, customer in enumerate(customers):
        if index:
            print()
        customer.go_shopping(shops, fuel_price)
