import os
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_path, "r") as info:
        information = json.load(info)

    fuel_price = information["FUEL_PRICE"]

    shops = [
        Shop(**shop)
        for shop in information["shops"]
    ]

    customers = [
        Customer(**client)
        for client in information["customers"]
    ]

    for customer in customers:
        customer.show_customers_wallet()
        Customer.customer_shop_trip(customer, shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
