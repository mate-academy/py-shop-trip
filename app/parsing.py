import os
import json


def parse_data_from_json() -> dict:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    customers_data = config["customers"]

    car_data = None
    for customer in customers_data:
        if "car" in customer:
            car_data = customer["car"]
            break

    if car_data is not None:
        config["car"] = car_data

    return config
