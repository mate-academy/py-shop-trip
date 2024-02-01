import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def unpacker(information_file: str) -> tuple:
    with open(information_file, "r") as config:
        data = json.load(config)
    customers = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"],
                 Car(customer["car"]["brand"],
                     customer["car"]["fuel_consumption"]))
        for customer in data["customers"]
    ]
    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in data["shops"]
    ]
    return customers, shops, data["FUEL_PRICE"]
