from app.customer import Customer
from app.car import Car
from app.shop import Shop
import json


def process_json_data() -> list:
    customers = []
    shops = []

    with open("app/config.json") as file:
        data = json.load(file)

        fuel_price = data["FUEL_PRICE"]

        for customer in data["customers"]:
            customers.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car(
                        customer["car"]["brand"],
                        customer["car"]["fuel_consumption"]
                    )
                )
            )

        for shop in data["shops"]:
            shops.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"],
                )
            )

    return [fuel_price, customers, shops]
