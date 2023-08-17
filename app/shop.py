import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Shop:
    name: str
    location: List
    products: dict


def create_shops() -> list:
    json_path = os.path.join("app", "config.json")
    with open(json_path, "r") as json_file:
        shops = json.load(json_file)["shops"]

    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in shops
    ]
