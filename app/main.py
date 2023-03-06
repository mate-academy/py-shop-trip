import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    shops = []
    with open("app/config.json") as file:
        app_data = json.load(file)
    Car.fuel_price = app_data["FUEL_PRICE"]
    for customer in app_data["customers"]:
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
    for shop in app_data["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers:
        customer.make_purchase(shops)
