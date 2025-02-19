import json

from app.customer import create_customers
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in create_customers(config["customers"]):
        customer.visit_shop(shops, fuel_price)


shop_trip()
