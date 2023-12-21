import json

from app.customer import Customer
from app.shop import Shop


def extract_json(json_file: str) -> tuple[list[Customer], list[Shop], float]:
    with open(json_file, "r") as json_file:
        data = json.load(json_file)
    row_customers = data["customers"]
    obj_customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        for customer in row_customers
    ]
    row_shops = data["shops"]
    obj_shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in row_shops
    ]
    return obj_customers, obj_shops, data["FUEL_PRICE"]
