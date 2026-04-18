import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(shop) for shop in config["shops"]]

    for customer_dct in config["customers"]:
        if config["customers"][0] != customer_dct:
            print("")
        customer = Customer(customer_dct, fuel_price)
        customer.get_the_cheapest_one(shops)
