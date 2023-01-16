import json
from typing import List

from app.customer import Customer
from app.shop import Shop


def read_customer_json() -> List[Customer]:
    customer_list = []
    try:
        with open("app/config.json", "r") as config:
            customers = json.load(config)
            customer_list = []
            for customer in customers["customers"]:
                customer_list.append(Customer(**customer))
    except FileNotFoundError:
        print("File do not found")
    return customer_list


def read_shop_json() -> List[Shop]:
    shops_list = []
    try:
        with open("app/config.json", "r") as config:
            shops = json.load(config)
            shops_list = []
            for shop in shops["shops"]:
                shops_list.append(Shop(**shop))
    except FileNotFoundError:
        print("File do not found")
    return shops_list


def fuel_price() -> float:
    with open("app/config.json", "r") as config:
        data = json.load(config)
        fuel_price = data["FUEL_PRICE"]
    return fuel_price
