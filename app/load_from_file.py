import json
import os


def get_dict_from_json_file() -> dict:
    json_path = os.path.join("app", "config.json")
    with open(json_path, "r") as json_file:
        json_dict = json.load(json_file)
    return json_dict
