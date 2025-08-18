import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**cust) for cust in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        customer.try_shopping(shops, fuel_price)
