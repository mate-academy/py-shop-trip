import json
import os


def load_config() -> dict:
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")
    with open(config_path, "r") as file:
        return json.load(file)
