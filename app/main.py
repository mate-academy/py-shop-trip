import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    price_per_liter = config.get("FUEL_PRICE")

    customer_list = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        )
        for customer in config["customers"]
    ]

    shop_list = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]

    for person in customer_list:
        person.trip_cost(shop_list, price_per_liter)
