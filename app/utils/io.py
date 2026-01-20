import json


def read_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
