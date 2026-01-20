import json
import os


def load_config() -> dict:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        config_data = json.load(file)
    return config_data


config = load_config()
