import json


def get_information() -> dict:
    with open(r"app\config.json") as file:
        info = json.load(file)
        return info
