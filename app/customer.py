from dataclasses import dataclass
import json


@dataclass
class Customers:

    name: str
    product_cart: dict
    location: list
    money: int
    car: dict
    list_of_customers = []

    @classmethod
    def create_customers(cls, config: str) -> None:
        with open(config) as f:
            file_ = json.load(f)
        for customer in file_["customers"]:
            cls.list_of_customers.append(Customers(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            ))
