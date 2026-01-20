from app.shop import Shop
from app.customer import Customer
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(
            person["name"],
            person["product_cart"],
            person["location"],
            person["money"],
            person["car"]["fuel_consumption"]
        )
        for person in config["customers"]
    ]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]

    for customer in customers:
        customer.cheapest_trip(shops, fuel_price)
