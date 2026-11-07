import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(**customer["car"]),
        )
        for customer in config["customers"]
    ]

    for index, customer in enumerate(customers):
        if index:
            print()
        customer.go_shopping(shops, fuel_price)
