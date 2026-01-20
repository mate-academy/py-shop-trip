import json
from typing import List


def load_json(filename: str) -> List[dict]:
    with open(filename, "r") as file:
        data = json.load(file)
    return data
