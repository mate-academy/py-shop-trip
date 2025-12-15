import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config_info = json.load(config)
        Car.FUEL_PRICE = config_info["FUEL_PRICE"]
        customers = [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"]
            )
            for customer in config_info["customers"]
        ]
        shops = [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in config_info["shops"]
        ]

        for customer in customers:
            customer.store_selection(shops)
