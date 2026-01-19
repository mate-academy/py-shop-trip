import json

from app.structures.customer_profile import Car, Customer
from app.structures.shop import Shop


def get_data(filename: str) -> dict:
    with open(filename, "r") as file:
        data_dict = json.load(file)
    return data_dict


def create_account(customer: dict) -> Customer:
    client = Customer(**customer)
    client.car = Car(client.car["brand"], client.car["fuel_consumption"])
    return client


def create_shop(shop: dict) -> Shop:
    shop = Shop(**shop)
    return shop
