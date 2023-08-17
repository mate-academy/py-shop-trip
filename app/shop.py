import json
from dataclasses import dataclass
from typing import List


@dataclass
class Shop:
    name: str
    location: List
    products: dict


with open(r"E:\projects\py-shop-trip\app\config.json", "r") as json_file:
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
