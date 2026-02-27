import json
import pathlib

from app.customer import Customer
from app.car import Car
from app.shop import Shop

FILE_PATH = pathlib.Path(__file__).parent / "config.json"


def shop_trip() -> None:
    with open(FILE_PATH, "r") as file:
        customers = []
        shops = []

        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customer_data = data["customers"]
        shops_data = data["shops"]

        for customer in customer_data:
            customers.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car(**customer["car"]),
                )
            )

        for shop in shops_data:
            shops.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"],
                )
            )

        for customer in customers:
            customer.greet()
            for shop in shops:
                customer.calc_trip_to_shop(shop, fuel_price)
            customer.ride_for_shopping()


shop_trip()
