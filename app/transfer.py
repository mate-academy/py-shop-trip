import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def transfer() -> list:
    with open("app/config.json") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    list_customers = []
    list_shops = []
    for customer, shop in zip(config["customers"], config["shops"]):
        list_customers.append(Customer(
            customer["name"], customer["product_cart"],
            customer["location"], customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        ))
        list_shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))
    return [fuel_price, list_customers, list_shops]
