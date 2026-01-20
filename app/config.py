import json

from app.customer import Customer, Car
from app.shop import Shop


with open("app/config.json", "r") as config_file:
    data = json.load(config_file)

CUSTOMERS = []
SHOPS = []
FUEL_PRICE = data["FUEL_PRICE"]

for customer in data["customers"]:
    CUSTOMERS.append(
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
    )

for shop in data["shops"]:
    SHOPS.append(
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
    )
