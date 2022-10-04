import json
from customers import Customer
from shops import Shop

with open("app/config.json") as json_file:
    config = json.load(json_file)


customers = []
shops = []
for customer in config["customers"]:
    customers.append(
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]["fuel_consumption"],
            customer["car"]
        )
    )
for shop in config["shops"]:
    shops.append(Shop(shop["name"], shop["location"], shop["products"]))


def customers_shops():
    return customers, shops
