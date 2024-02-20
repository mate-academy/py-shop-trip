from dataclasses import dataclass

from app.get_info import info_from_file
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car


customers = {}

for customer in info_from_file["customers"]:
    customers[customer["name"]] = Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
    )
