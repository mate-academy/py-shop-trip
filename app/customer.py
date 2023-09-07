import json
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")


def customers_and_content() -> list:
    with open(relative_path, "r") as file:
        content = json.load(file)
    return content


class Customer:
    def __init__(
            self,
            location: dict,
            fuel_consumption: list,
            priсe_fuel: dict,
            money: dict,
            name: str,
            product: dict,
    ) -> dict:
        self.location = location
        self.fuel_consumption = fuel_consumption
        self.priсe_fuel = priсe_fuel
        self.money = money
        self.name = name
        self.product = product
