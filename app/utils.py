import json
import os

from app.customer import create_customers_from_list
from app.shop import create_shop_from_list


def read_json_file(file_name: str) -> dict:
    dir_name = os.path.dirname(os.path.abspath(__file__))
    full_file_name = os.path.join(dir_name, file_name)
    with open(full_file_name) as config_file:
        config_data = json.load(config_file)

    return config_data


def unpacking_file_data(data: dict) -> dict:
    clear_data = {}
    for key in data:
        if isinstance(data[key], (float, int)):
            clear_data[key] = data[key]
            continue

        if key == "customers":
            clear_data[key] = create_customers_from_list(data[key])
            continue

        if key == "shops":
            clear_data[key] = create_shop_from_list(data[key])

    return clear_data
