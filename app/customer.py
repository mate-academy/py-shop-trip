import json

from typing import List
from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    products: dict
    location: list[int, int]
    money: float
    car: dict


def customer_initial() -> List[Customer]:
    customers = []
    with open("app/config.json", "r") as file:
        data = json.load(file)
        for idx in range(len(data["customers"])):
            customers.append(
                Customer(
                    data["customers"][idx]["name"],
                    data["customers"][idx]["product_cart"],
                    data["customers"][idx]["location"],
                    data["customers"][idx]["money"],
                    data["customers"][idx]["car"]
                )
            )
    return customers
