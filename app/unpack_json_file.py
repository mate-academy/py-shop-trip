import json
from typing import Any


def unpack(json_file: json, data_name: str) -> Any:
    with open(json_file, "r") as file:
        data = json.load(file)
        if data_name == "fuel_price":
            return data["FUEL_PRICE"]
        if data_name == "customers":
            return data["customers"]
        if data_name == "shops":
            return data["shops"]
