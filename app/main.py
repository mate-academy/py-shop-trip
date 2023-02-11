import json
import os
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shops


def shop_trip() -> None:
    path_ = Path(__file__).parent.parent
    file_ = os.path.join(path_, "app", "config.json")
    with open(file_) as config_json:
        data_json = json.load(config_json)
    fuel_price = data_json["FUEL_PRICE"]
    shop_data = []
    customers_data = []
    for customer in data_json["customers"]:
        customers_data.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_for_100_km=customer["car"]["fuel_consumption"]
            ),
        ))

    for shop in data_json["shops"]:
        shop_data.append(Shops(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ))

    for customer in customers_data:
        customer.get_best_option(fuel_price, shop_data)


if __name__ == "__main__":
    shop_trip()
