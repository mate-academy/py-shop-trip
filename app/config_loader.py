import os
import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def read_config() -> dict:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        data = json.load(file)

    return data


def build_customers(config: dict) -> list:
    customers_data = config["customers"]
    customers = []

    for customer_data in customers_data:
        car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"]
        )
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            car
        )

        customers.append(customer)

    return customers


def build_shops(config: dict) -> list:
    shops_data = config["shops"]
    shops = []

    for shop_data in shops_data:
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )

        shops.append(shop)

    return shops
