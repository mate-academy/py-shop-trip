import json
import os
from app.cars import Car
from app.customers import Customer
from app.shops import Shop


def load_file(file_name: str) -> dict:
    with open(os.path.join("app", file_name), "r") as file:
        return json.load(file)


def get_fuel_price(data: dict) -> None:
    Car.fuel_price = data["FUEL_PRICE"]


def create_customers(data: dict) -> list:
    return [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"],
                 customer["car"])
        for customer in data["customers"]
    ]


def create_shops(data: dict) -> list:
    return [
        Shop(shop["name"],
             shop["location"],
             shop["products"])
        for shop in data["shops"]
    ]
