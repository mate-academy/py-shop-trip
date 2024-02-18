import json
from os import path

from app.customer import Customer
from app.car import Car
from app.shop import Shop

project_dir = path.dirname(path.dirname(path.abspath(__file__)))
config_file = path.join(project_dir, "app/config.json")

with open(config_file, "r") as file:
    config = json.load(file)

FUEL_PRICE = config.get("FUEL_PRICE")

customers = {}
for customer in config.get("customers"):
    customers[customer.get("name")] = Customer(
        customer.get("name"),
        customer.get("product_cart"),
        customer.get("location"),
        customer.get("money"),
        Car(
            customer.get("car").get("brand"),
            customer.get("car").get("fuel_consumption")
        )
    )

shops = {}
for shop in config.get("shops"):
    shops[shop.get("name")] = Shop(
        shop.get("name"),
        shop.get("location"),
        shop.get("products")
    )
