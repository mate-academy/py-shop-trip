import os
import json


def data_loading() -> dict:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "config.json")

    with open(file_path, "r") as file:
        configs = json.load(file)

    return configs
