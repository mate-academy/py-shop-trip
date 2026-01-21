import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def parse_customers() -> list[Customer]:
    customers_objects = []
    with open("app/config.json") as config:
        customers = json.load(config)["customers"]
    for customer in customers:
        customers_objects.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(**customer["car"])
            )
        )
    return customers_objects


def parse_shops() -> list[Shop]:
    shops_objects = []
    with open("app/config.json") as config:
        shops = json.load(config)["shops"]
    for shop in shops:
        shops_objects.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )
    return shops_objects


def parse_fuel_price() -> float:
    with open("app/config.json") as config:
        return json.load(config)["FUEL_PRICE"]
