import json


def load_config() -> dict:
    with open("app/config.json") as file:
        return json.load(file)
