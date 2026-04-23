import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = (
        "app/config.json"
        if os.path.exists("app/config.json")
        else "config.json"
    )

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(s) for s in config["shops"]]
    customers = [Customer(c) for c in config["customers"]]

    for i, customer in enumerate(customers):
        customer.shop_trip(shops, fuel_price)
        if i < len(customers) - 1:
            print()
