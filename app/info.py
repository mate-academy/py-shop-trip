import json


def get_information() -> dict:
    with open("app/config.json", "r") as file:
        info = json.load(file)
        return info
