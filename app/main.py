import json
import os

from app.customer import Customer
from app.car import Car
from app.shop import Shop

CONFIG_FILE = "config.json"


def shop_trip() -> None:
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, CONFIG_FILE), "r") as config:
        info = json.load(config)

    customers = create_customers(info["customers"])
    shops = create_shops(info["shops"])

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.calculate_all_cost(shops, info["FUEL_PRICE"])
        if shop := customer.target_shop:
            shop.print_bill(customer.name, customer.product_cart)
            customer.print_goodbye()


def create_customers(customers: dict) -> list[Customer]:
    return [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in customers
    ]


def create_shops(shops: dict) -> list[Shop]:
    return [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in shops
    ]


if __name__ == "__main__":
    shop_trip()
