import json
from pathlib import Path

from app.create_instances import create_customers, create_shops


def read_json_file() -> tuple:
    path_to_file = Path(__file__).parent.joinpath("config.json")
    with open(path_to_file, "r") as file_read_stream:
        file_data = json.load(file_read_stream)

    fuel_price = file_data["FUEL_PRICE"]
    customers = create_customers(file_data["customers"])
    shops = create_shops(file_data["shops"])

    return customers, shops, fuel_price
