import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def unpacker(information_file: str) -> tuple:
    with open(information_file, "r") as config:
        data = json.load(config)
    customers = []
    shops = []
    for customer in data["customers"]:
        customers.append(
            Customer(customer["name"],
                     customer["product_cart"],
                     customer["location"],
                     customer["money"],
                     Car(customer["car"]["brand"],
                         customer["car"]["fuel_consumption"]))
        )
    for shop in data["shops"]:
        shops.append(
            Shop(shop["name"], shop["location"], shop["products"])
        )

    return customers, shops, data["FUEL_PRICE"]
