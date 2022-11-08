import json

from app.model.customer import Customer
from app.model.shop import Shop


def shop_trip():
    with open("app/config.json", "r") as config:
        config_data = json.load(config)
        customers = {data["name"]: Customer(data["name"],
                                            data["product_cart"],
                                            data["location"],
                                            data["money"],
                                            data["car"])
                     for data
                     in config_data["customers"]}
        shops = {shop_data["name"]: Shop(shop_data["name"],
                                         shop_data["location"],
                                         shop_data["products"])
                 for shop_data
                 in config_data["shops"]}

        for customer in customers.values():
            customer.go_shopping(config_data["FUEL_PRICE"], shops)
