from app.car import Car
from app.customer import Customer
from app.shop import Shop
import json


def read_file(file_name: str, mode: str = "r") -> dict:
    with open(file_name, mode) as file_content:
        content = json.load(file_content)
        fuel_price = content["FUEL_PRICE"]
        customers = content["customers"]
        shops = content["shops"]
        customers_instances = []
        shops_instances = []

        for customer in customers:
            new_customer = Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )
            customers_instances.append(new_customer)

        for shop in shops:
            new_shop = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            shops_instances.append(new_shop)

    return {
        "fuel_price": fuel_price,
        "customers": customers_instances,
        "shops": shops_instances
    }
