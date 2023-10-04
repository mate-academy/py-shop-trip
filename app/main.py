import json

from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)
    shops = config["shops"]
    customers = config["customers"]
    shop_classes = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in shops
    ]
    for customer in customers:
        customer_class = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
                config["FUEL_PRICE"])
        )
        customer_class.buy(shop_classes)
