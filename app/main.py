import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    shops = []
    with open("app/config.json", "r") as config_file:
        info = json.load(config_file)
        fuel_price = info["FUEL_PRICE"]

        for customer in info["customers"]:
            customers.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car(
                        customer["car"]["brand"],
                        customer["car"]["fuel_consumption"],
                    )
                )
            )
        for shop in info["shops"]:
            shops.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"],
                )
            )

    for customer in customers:
        customer.acting(shops, fuel_price)
