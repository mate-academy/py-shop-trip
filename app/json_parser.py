import json
from typing import Any


def read_json_from_file(file_path: str) -> Any:
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not fount: {file_path}")


def get_customers_data(json_data: Any) -> list:
    return json_data.get("customers")


def get_shops_data(json_data: Any) -> list:
    return json_data.get("shops")


def get_fuel_price(json_data: Any) -> float:
    return json_data.get("FUEL_PRICE")
