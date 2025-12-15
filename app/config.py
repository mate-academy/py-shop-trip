import json


def load_config(filename: str) -> dict:
    with open(f"app/{filename}", "r") as file:
        return json.load(file)
