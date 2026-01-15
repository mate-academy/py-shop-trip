import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    """Load config, create objects and launch shopping simulation."""
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as json_data:
        data = json.load(json_data)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**c) for c in data["customers"]]
    shops = [Shop(**s) for s in data["shops"]]

    for customer in customers:
        customer.preparation(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
