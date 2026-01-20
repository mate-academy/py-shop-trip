import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as config:
        data = json.load(config)

    fuel_price = data["FUEL_PRICE"]

    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        customer.shopping(shops, fuel_price)
