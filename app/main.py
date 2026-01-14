import json
import os
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as config_json:
        config_data = json.load(config_json)

    shops = [
        Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        ) for shop_data in config_data["shops"]
    ]

    customers = []
    for customer_data in config_data["customers"]:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car,
            fuel_price=config_data["FUEL_PRICE"]
        )
        customers.append(customer)

    for customer in customers:
        customer.choose_shop(shops)
