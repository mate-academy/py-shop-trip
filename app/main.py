import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = file.read()
    config = json.loads(config)
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            ),
            config["FUEL_PRICE"],
        )
        for customer in config["customers"]
    ]
    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]
    for customer in customers:
        customer.go_to_shopping(shops)


if __name__ == "__main__":
    shop_trip()
