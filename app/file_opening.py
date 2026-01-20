import os
import json

from app.customer import Customer
from app.shop import Shop


def file_open(name_of_file: str) -> dict:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, name_of_file)
    with open(config_path) as f:
        person_data = json.load(f)
        shops = [Shop(shop) for shop in person_data["shops"]]
        customers = [
            Customer(customer) for customer in person_data["customers"]
        ]
        fuel_price = person_data["FUEL_PRICE"]
        return {
            "fuel_price": fuel_price,
            "shops": shops,
            "customers": customers
        }
