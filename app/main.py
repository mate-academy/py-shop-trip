from __future__ import annotations

import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop.from_dict(data) for data in config["shops"]]
    customers = [Customer.from_dict(data) for data in config["customers"]]

    reports = (
        customer.describe_trip(shops, fuel_price) for customer in customers
    )
    print("\n\n".join(reports))
