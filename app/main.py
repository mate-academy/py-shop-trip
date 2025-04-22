import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer.config_from_dict(customer)
                 for customer
                 in config["customers"]]
    shops = [Shop.config_from_dict(shop)
             for shop
             in config["shops"]]

    for customer in customers:
        customer.check_shops(fuel_price, shops)
