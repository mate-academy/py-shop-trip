import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def export_data() -> None:
    with open("app/config.json", "r") as file:
        content = json.load(file)

    customers = content["customers"]
    for customer in customers:
        Customer(customer["name"], customer["product_cart"],
                 customer["location"], customer["money"],
                 Car(customer["car"]["brand"],
                     customer["car"]["fuel_consumption"],
                     content["FUEL_PRICE"]))

    shops = content["shops"]
    for shop in shops:
        Shop(shop["name"], shop["location"], shop["products"])
