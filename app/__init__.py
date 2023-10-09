import json
import os
from app.customer import Customer
from app.shop import Shop


def get_data(file_name: str) -> tuple | None:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print(current_dir)
        print("File not found!")
        return

    if all(key in content for key in ("FUEL_PRICE", "customers", "shops")):
        customer_list = []
        shop_list = []
        fuel_price = content["FUEL_PRICE"]

        for client in content["customers"]:
            if client:
                customer_list.append(Customer(**client))
        for store in content["shops"]:
            if store:
                shop_list.append(Shop(**store))
        return customer_list, shop_list, fuel_price,
