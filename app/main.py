import json

from app.customer import Customers
from app.shop import Shop
from app.car import Car


def shop_trip():
    with open("config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = Customers.create_customer(data["customers"])
        shops = data["shops"]
        print(customers[0].money)
    return

shop_trip()


