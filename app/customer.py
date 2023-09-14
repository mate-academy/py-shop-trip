from app.load_from_file import get_dict_from_json_file
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
    customers = get_dict_from_json_file()["customers"]
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
