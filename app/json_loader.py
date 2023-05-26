import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def get_info_from_json() -> dict:
    with open(BASE_DIR / "config.json") as file:
        return json.load(file)


def get_shops() -> dict:
    shops = {}
    for name in get_info_from_json()["shops"]:
        shops[name["name"]] = {
            "location": name["location"],
            "products": name["products"]
        }
    return shops


def get_customers() -> list[dict]:
    return get_info_from_json()["customers"]


def get_fuel_price() -> (int, float):
    return get_info_from_json()["FUEL_PRICE"]
