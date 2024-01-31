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
        customers_instances = [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(**customer["car"])
            )
            for customer in customers
        ]
        shops_instances = [Shop(**shop) for shop in shops]

    return {
        "fuel_price": fuel_price,
        "customers": customers_instances,
        "shops": shops_instances
    }
