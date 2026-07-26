import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    """Send every customer to the cheapest shop they can afford."""
    app_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(app_dir, "config.json")

    if not os.path.exists(config_path):
        config_path = os.path.join(os.path.dirname(app_dir), "config.json")

    with open(config_path, "r") as file:
        config = json.load(file)

    shops = [Shop(**shop_data) for shop_data in config["shops"]]
    customers = [
        Customer.from_dict(customer_data)
        for customer_data in config["customers"]
    ]

    for index, customer in enumerate(customers):
        if index:
            print()

        customer.make_trip(shops, config["FUEL_PRICE"])
