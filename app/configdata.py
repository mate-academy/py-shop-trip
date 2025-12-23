import json
import os

from typing import List, Dict, Any
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def load_config(file_name: str = "config.json") -> Dict[str, Any]:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, "r") as file:
        return json.load(file)


def create_customers(customers_data: List[dict[str, Any]]) -> List[Customer]:

    customers = []

    for cust_data in customers_data:
        car = Car(
            brand=cust_data["car"]["brand"],
            fuel_consumption=cust_data["car"]["fuel_consumption"]
        )

        customer = Customer(
            name=cust_data["name"],
            money=cust_data["money"],
            car=car,
            product_cart=cust_data["product_cart"],
            location=cust_data["location"],
        )

        customers.append(customer)

    return customers


def create_shop(shop_data: List[Dict[str, Any]]) -> List[Shop]:

    shops = []

    for shop in shop_data:
        shop_instance = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        shops.append(shop_instance)

    return shops
