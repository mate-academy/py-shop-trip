import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List
    money: float
    car: dict


json_path = os.path.join("app", "config.json")
with open(json_path, "r") as json_file:
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
