import json


def config_loader(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)
