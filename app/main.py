import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file_config:
        config = json.load(file_config)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in config["customers"]:
        Customer(**customer).go_shopping(fuel_price, shops)
