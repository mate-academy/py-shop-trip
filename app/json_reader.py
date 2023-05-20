import json
import os


def read_file() -> None:
    path_file = os.path.abspath(".")
    path_file = os.path.join(path_file, "app", "config.json")
    with open(path_file, "r") as config:
        data = json.load(config)
        fuel_price = data["FUEL_PRICE"]
        return data, fuel_price
