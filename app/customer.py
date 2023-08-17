import json
from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List
    money: float
    car: dict


with open(r"E:\projects\py-shop-trip\app\config.json", "r") as json_file:
    customers = json.load(json_file)["customers"]

    customer_class = []
    for customer in customers:
        customer_class.append(
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"]
            )
        )
