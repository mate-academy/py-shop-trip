import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: float
    car: dict


def create_customers() -> List[Customer]:
    json_path = os.path.join("app", "config.json")
    with open(json_path, "r") as json_file:
        customers = json.load(json_file)["customers"]
        return [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"]
            )
            for customer in customers
        ]
