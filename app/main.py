import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_cost = data["FUEL_PRICE"]

    customers = [
        Customer(
            customer_dict["name"],
            customer_dict["product_cart"],
            customer_dict["location"],
            customer_dict["money"],

            Car(
                customer_dict["car"]["brand"],
                customer_dict["car"]["fuel_consumption"]
            )
        ) for customer_dict in data["customers"]
    ]

    shops = [
        Shop(
            shop_dict["name"],
            shop_dict["location"],
            shop_dict["products"]
        ) for shop_dict in data["shops"]
    ]

