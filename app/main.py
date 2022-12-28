import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as source_file:
        customers_and_shops = json.load(source_file)

        customers = [
            Customer(
                customer_data,
                customers_and_shops["FUEL_PRICE"]
            )
            for customer_data in customers_and_shops["customers"]
        ]

        shops = [
            Shop(shop_data)
            for shop_data in customers_and_shops["shops"]
        ]

        for customer in customers:
            customer.go_shopping(shops, Car(
                customer.location,
                customer.car["fuel_consumption"]))

shop_trip()
