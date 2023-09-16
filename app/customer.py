import json
import os
from app.car import Car


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
RELATIVE_PATH = os.path.join(CURRENT_DIRECTORY, "config.json")


def components_file() -> None:
    with open(RELATIVE_PATH, "r") as file:
        content = json.load(file)
    customers = content.get("customers")
    shops = content.get("shops")
    priсe_fuel = content.get("FUEL_PRICE")
    return customers, shops, priсe_fuel


class Customer:
    def __init__(
            self, car: dict,
            product_cart: dict,
            name: str,
            location: list,
            money: int
    ) -> None:
        self.car = Car(**car)
        self.name = name
        self.location = location
        self.product_cart = product_cart
        self.money = money
