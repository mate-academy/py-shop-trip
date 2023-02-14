import json
import os
from typing import Any
from pathlib import Path
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_data_from_json() -> list:
    path_ = Path(__file__).parent.parent
    file_ = os.path.join(path_, "app", "config.json")
    with open(file_) as config_json:
        data_json = json.load(config_json)
    return data_json


def get_customer_data(data_json: Any) -> list[Customer]:
    customers_data = []
    for customer in data_json["customers"]:
        customers_data.append(Customer(
            name=dict.get(customer, "name"),
            product_cart=dict.get(customer, "product_cart"),
            location=dict.get(customer, "location"),
            money=dict.get(customer, "money"),
            car=Car(
                brand=dict.get(customer["car"], "brand"),
                fuel_for_100_km=dict.get(customer["car"], "fuel_consumption")
            ),
        ))
    return customers_data


def get_shop_data(data_json: Any) -> list[Shop]:
    shops_data = []
    for shop in data_json["shops"]:
        shops_data.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ))
    return shops_data


def shop_trip() -> None:
    data_json = load_data_from_json()
    customers = get_customer_data(data_json)
    shops = get_shop_data(data_json)
    fuel_price = data_json["FUEL_PRICE"]

    for customer in customers:
        customer.get_best_option(fuel_price, shops)


if __name__ == "__main__":
    shop_trip()
