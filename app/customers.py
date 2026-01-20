import json
from pathlib import Path


class Customers:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


def create_customer_objects() -> list:
    base_dir = Path(__file__).resolve().parent

    with open(base_dir / "config.json", "r") as file:
        data = json.load(file)
        customers = data["customers"]
        customers_list = []
        for customer in customers:
            customer_obj = Customers(name=customer["name"],
                                     product_cart=customer["product_cart"],
                                     location=customer["location"],
                                     money=customer["money"],
                                     car=customer["car"])
            customers_list.append(customer_obj)
    return customers_list
