import json


def get_data() -> json:
    """Return data from json file."""
    with open("app/config.json", "r") as file_object:
        return json.load(file_object)
