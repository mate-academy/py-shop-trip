import os
import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def prepare_for_shop_trip() -> tuple:
    with open(os.path.join("app", "config.json")) as data_file:
        json_str = data_file.read()

    data_dict = json.loads(json_str)

    customers_list = [
        Customer(customer, Car(data_dict["FUEL_PRICE"], customer["car"]))
        for customer in data_dict["customers"]
    ]

    shops_list = [
        Shop(shop)
        for shop in data_dict["shops"]
    ]

    return customers_list, shops_list


customers, shops = prepare_for_shop_trip()
