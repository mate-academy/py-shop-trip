from typing import Dict
import dataclasses
import json
import os


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict


def convert_file() -> Dict:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as file:
        file_content = json.load(file)
    return file_content


def create_customers() -> list:
    return [Customer(
        name=person["name"],
        product_cart=person["product_cart"],
        location=person["location"],
        money=person["money"],
        car=person["car"]
    ) for person in convert_file()["customers"]]
