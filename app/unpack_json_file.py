import json
from typing import Any


def unpack(json_file: str, data_name: str) -> Any:
    with open(json_file, "r") as file:
        data = json.load(file)
        if data_name == "fuel_price":
            return data["FUEL_PRICE"]
        elif data_name == "customers":
            return data["customers"]
        elif data_name == "shops":
            return data["shops"]
        else:
            return None
