import json
import os

from app.customer.customer_class import Customer


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as file:
        data = json.load(file)

    for customer_detail in data["customers"]:
        customer = Customer(customer_detail, data["FUEL_PRICE"])
        customer.go_to_shop(data["shops"])


if __name__ == "__main__":
    shop_trip()
