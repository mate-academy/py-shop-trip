import json
import os
from app.customers import Customer
from app.shops import Shop


def load_file(file_name: str) -> dict:
    with open(os.path.join("app", file_name), "r") as file:
        return json.load(file)


def create_customers(data: dict) -> list:
    return [
        Customer(**customer)
        for customer in data["customers"]
    ]


def create_shops(data: dict) -> list:
    return [
        Shop(**shop)
        for shop in data["shops"]
    ]
