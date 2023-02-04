import json

from app.customer import Customers
from app.shops import Shops


def shop_trip():
    with open("app.config.json", "r") as data_file:
        config_file = json.load(data_file)
        for customer in config_file["customers"]:
            person = Customers(customer)
        for shop in config_file["shops"]:
            Shops(shop)
