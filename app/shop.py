import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Shop:
    name: str
    location: List
    products: dict


json_path = os.path.join("app", "config.json")
with open(json_path, "r") as json_file:
    shops = json.load(json_file)["shops"]

    shop_class = []
    for shop in shops:
        shop_class.append(
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
        )
