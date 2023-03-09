import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


# Name and path to file with data
file_name = "app/config.json"


def get_dict_from_json(json_file_name: str) -> dict:
    with open(json_file_name, "r") as data_file:
        return json.load(data_file)


def create_shop_objects() -> tuple:
    data_dict = get_dict_from_json(file_name)
    return tuple([Shop(
        store["name"],
        store["location"],
        store["products"]
    ) for store in data_dict["shops"]])


def create_customer_objects() -> tuple:
    data_dict = get_dict_from_json(file_name)
    fuel_price = data_dict["FUEL_PRICE"]
    return tuple([Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"],
            fuel_price
        )
    ) for customer in data_dict["customers"]])
