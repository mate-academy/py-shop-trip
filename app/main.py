import json

from app.customer import Customer
from app.shop import Shop
from app.trip import trip


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    customers = []
    for customer in config["customers"]:
        customer = Customer(**customer)
        customers.append(customer)

    shops = []
    for shop in config["shops"]:
        shop = Shop(**shop)
        shops.append(shop)

    fuel_price = config["FUEL_PRICE"]
    for customer in customers:
        trip(customer, shops, fuel_price)
