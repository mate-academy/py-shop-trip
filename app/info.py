import json


def full_info(json_file: str) -> dict:
    with open(json_file, "r") as file:
        info = json.load(file)

    return info
