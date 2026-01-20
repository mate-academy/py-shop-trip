import json

from app.customer import Customers
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

        fuel_price = config["FUEL_PRICE"]
        shops = [Shop(**shop) for shop in config["shops"]]

        for customer in config["customers"]:
            Customers(**customer).go_shopping(fuel_price, shops)
