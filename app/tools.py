import json
from app.car import FuelPrice
from app.customer import Customer
from app.shop import Shop


def load_data(filename: str) -> list:
    with open(filename) as file_config_json:
        data = json.load(file_config_json)

    shops = [Shop(**shop) for shop in data["shops"]]
    customers = [Customer(**customer) for customer in data["customers"]]
    FuelPrice.value = data["FUEL_PRICE"]

    return (customers, shops)
