import json


def load_data(filename: str) -> dict:
    with open(filename, "r") as f:
        data = json.load(f)
    return data
