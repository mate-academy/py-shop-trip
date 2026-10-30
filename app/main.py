import json
from .classes.customer import Customer
from .classes.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)
        fuel_price = data["FUEL_PRICE"]
        customers = [
            Customer(**customer_dict) for customer_dict in data["customers"]
        ]
        shops = [Shop(**shop_dict) for shop_dict in data["shops"]]

    for customer_dict in customers:
        customer_dict.to_do_the_trip(shops, fuel_price)
