import json
import os
from app.car import Car


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")


def customers_and_content() -> list:
    with open(relative_path, "r") as file:
        content = json.load(file)
    customers = content.get("customers")
    shops = content.get("shops")
    priсe_fuel = content.get("FUEL_PRICE")
    return customers, shops, priсe_fuel


class Customer:
    def __init__(self, car: None, info: dict) -> None:
        self.car = Car(**car)
        self.name = info["name"]
        self.location = info["location"]
        self.product_cart = info["product_cart"]
        self.money = info["money"]
