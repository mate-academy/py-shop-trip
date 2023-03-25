import json
from typing import List, Dict

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def read_config_file(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def create_customers(customers_data: List[Dict[str, dict]]) -> List[Customer]:
    customers = [
        Customer(
            customer_dict.get("name"),
            customer_dict.get("product_cart"),
            customer_dict.get("location"),
            customer_dict.get("money"),
            Car(
                customer_dict.get("car", {}).get("brand"),
                customer_dict.get("car", {}).get("fuel_consumption")
            )
        ) for customer_dict in customers_data
    ]
    return customers


def create_shops(shops_data: List[Dict[str, dict]]) -> List[Shop]:
    shops = [
        Shop(
            shop_dict.get("name"),
            shop_dict.get("location"),
            shop_dict.get("products")
        ) for shop_dict in shops_data
    ]
    return shops


def process_customers(
        customers: List[Customer], shops: List[Shop], fuel_cost: float
) -> None:
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
