import json
from typing import List

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def read_config_file(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def create_customers(customers_data: List[dict]) -> list:
    customers = [
        Customer(
            customer_dict["name"],
            customer_dict["product_cart"],
            customer_dict["location"],
            customer_dict["money"],
            Car(
                customer_dict["car"]["brand"],
                customer_dict["car"]["fuel_consumption"]
            )
        ) for customer_dict in customers_data
    ]
    return customers


def create_shops(shops_data: List[dict]) -> list:
    shops = [
        Shop(
            shop_dict["name"],
            shop_dict["location"],
            shop_dict["products"]
        ) for shop_dict in shops_data
    ]
    return shops


def process_customers(customers: List[Customer], shops: list, fuel_cost: float) -> None:
    for customer in customers:
        print(customer.money_of_costomer)
        customer.bill_by_shop(shops, fuel_cost)


def shop_trip() -> None:
    config_data = read_config_file("app/config.json")

    fuel_cost = config_data["FUEL_PRICE"]
    customers = create_customers(config_data["customers"])
    shops = create_shops(config_data["shops"])

    process_customers(customers, shops, fuel_cost)


if __name__ == "__main__":
    shop_trip()
