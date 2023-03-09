import json


from app.distance import Distance
from app.customers import Customer
from app.shop import Shop

with open("app/config.json", "r") as config:
    data = json.load(config)


def shop_trip() -> None:
    distance = Distance()
    customers = [
        Customer(
            person["name"],
            person["money"],
            person["product_cart"],
            person["location"],
            person["car"]["fuel_consumption"],
        )
        for person in data["customers"]
    ]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]
    for customer in customers:
        customer.amount_of_money()
        customer.check_price(shops, distance, data["FUEL_PRICE"])
        customer.shopping(shops, distance, data["FUEL_PRICE"])
