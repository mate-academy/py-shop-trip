import json

from .parse_config import parse_config


def shop_trip():
    with open("app/config.json", "r") as file:
        config = json.load(file)

    customers, shops, fuel_price = parse_config(config)

    for customer in customers:
        customer.shop_trip(shops, fuel_price)
