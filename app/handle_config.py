import json
from typing import Any

from app.shop import shop_from_dict
from app.customer import customer_from_dict


def handle_config() -> Any:
    with open("app/config.json") as file:
        config = json.load(file)
    customers = [customer_from_dict(customer) for customer in config["customers"]]
    shops = [shop_from_dict(shop) for shop in config["shops"]]
    return config["FUEL_PRICE"], customers, shops
