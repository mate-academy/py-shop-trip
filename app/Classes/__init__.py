import json
import os
from app.Classes.customer import Customer
from app.Classes.shop import Shop


FUEL_PRICE = 0
CUSTOMER_LIST = []
SHOP_LIST = []


def get_data(file_name: str) -> dict | None:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", file_name)
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return

    if all(key in content for key in ("FUEL_PRICE", "customers", "shops")):
        global FUEL_PRICE
        global CUSTOMER_LIST
        global SHOP_LIST
        FUEL_PRICE = content["FUEL_PRICE"]
        for client in content["customers"]:
            if len(client) != 0:
                CUSTOMER_LIST.append(Customer(**client))
        for store in content["shops"]:
            if len(store) != 0:
                SHOP_LIST.append(Shop(**store))
