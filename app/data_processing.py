import os

import json

from app.customer import Customer
from app.shop import Shop

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "config.json")

with open(file_path, "r") as file:
    configs = json.load(file)

fuel_price = configs["FUEL_PRICE"]
customers = []
shops = []


def data_processing() -> None:
    for key, value in configs.items():
        if key == "customers":
            for customer in value:
                new_customer = Customer(customer)
                customers.append(new_customer)

        if key == "shops":
            for shop in value:
                new_shop = Shop(shop)
                shops.append(new_shop)
