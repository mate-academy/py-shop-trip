import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data.get("FUEL_PRICE")

    customers = [
        Customer(customer_dictionary)
        for customer_dictionary
        in data["customers"]
    ]
    shops = [
        Shop(shop_dictionary)
        for shop_dictionary
        in data["shops"]
    ]

    for customer in customers:
        customer.go_shopping(fuel_price, shops)
