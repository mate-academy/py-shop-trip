import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        customers_data = data["customers"]
        fuel_price = data["FUEL_PRICE"]
        shops_data = data["shops"]

    customers_objs = [
        Customer(*customer.values()) for customer in customers_data
    ]
    shops_objs = [Shop(*shop.values()) for shop in shops_data]

    for customer in customers_objs:
        customer.initial_amount()
        customer.price_of_trip(fuel_price, shops_objs)
