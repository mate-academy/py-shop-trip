import json
import os
import datetime


def load_config(file_path: str) -> dict:
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_path)

    with open(full_path, "r") as file:
        config = json.load(file)
    return config


def get_current_time() -> None:
    return datetime.datetime.now()
