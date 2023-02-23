import json

from app.customer import Customer
from app.shop import Shop


def read_json() -> dict:
    with open("app/config.json", "r") as file_open:
        data = json.load(file_open)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    info_dict = {
        "customers": customers,
        "shops": shops,
        "fuel_price": fuel_price
    }

    return info_dict
