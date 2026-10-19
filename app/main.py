import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")
    if not os.path.exists(config_path):
        config_path = os.path.join(os.path.dirname(base_dir), "config.json")

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(s["name"], s["location"], s["products"])
        for s in config["shops"]
    ]
    customers = [
        Customer(
            c["name"],
            c["product_cart"],
            c["location"],
            c["money"],
            c["car"],
        )
        for c in config["customers"]
    ]

    for customer in customers:
        customer.process_shopping(shops, fuel_price)
