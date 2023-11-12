import json
import os


path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.json"))


def get_data() -> dict:
    with open(path, "r") as text:
        data = json.load(text)
    return data
