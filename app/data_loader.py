import json
import os
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def load_data() -> dict:
    config_path = os.path.join("app", "config.json")
    with open(config_path, "r") as file:
        data = json.load(file)
    customers = []
    shops = []
    for customer in data["customers"]:
        customers.append(Customer(customer["name"],
                                  customer["product_cart"],
                                  customer["location"],
                                  customer["money"],
                                  Car(customer["car"]["brand"],
                                      customer["car"]["fuel_consumption"])
                                  )
                         )
    for shop in data["shops"]:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))

    return {"customers": customers, "shops": shops, "fuel_price": data["FUEL_PRICE"]}
