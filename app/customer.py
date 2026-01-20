import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as customer_file:
    dane = json.load(customer_file)


def customers() -> list[dict]:
    return dane["customers"]
