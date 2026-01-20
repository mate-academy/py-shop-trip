import json

from app.customers import Customers


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)
    for customer in config["customers"]:
        Customers(customer).customer_money()
        Customers(customer).cheap_trip(config["shops"], config["FUEL_PRICE"])


shop_trip()
