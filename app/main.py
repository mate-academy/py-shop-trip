import json
from os import path

from app.customer import Customer


def shop_trip() -> None:
    with open(path.join("app", "config.json"), "r") as file:
        info = json.load(file)

    fuel_info = info["FUEL_PRICE"]
    customers_info = info["customers"]
    shop_info = info["shops"]
    if customers_info:
        for customer in customers_info:
            Customer(customer).customer_money()
            Customer(customer).cheaper_shop(shop_info, fuel_info)
