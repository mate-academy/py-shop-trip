import json
from pathlib import Path


def open_json_file() -> dict:
    file_path = Path(__file__).parent / "config.json"

    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data
