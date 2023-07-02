import json
from os import path

from app.customer import Customer
from app.shop import Shop
from app.shopping_trip import ShoppingTrip


def shop_trip() -> None:
    file_name = path.join("app", "config.json")

    with open(file_name, "r") as file:
        data = json.load(file)

        fuel_price = data["FUEL_PRICE"]
        shops = [Shop(**shop) for shop in data["shops"]]

        for customer in data["customers"]:
            customer = Customer(**customer)
            shopping_trip = ShoppingTrip(shops, customer, fuel_price)
            shopping_trip.go_to_shop()
