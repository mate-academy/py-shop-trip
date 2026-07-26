import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    """Send every customer to the cheapest shop they can afford."""
    with open("config.json", "r") as file:
        config = json.load(file)

    shops = [Shop(**shop_data) for shop_data in config["shops"]]
    customers = [
        Customer.from_dict(customer_data)
        for customer_data in config["customers"]
    ]

    for customer in customers:
        customer.make_trip(shops, config["FUEL_PRICE"])
