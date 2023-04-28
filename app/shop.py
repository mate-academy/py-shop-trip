import json
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict


with open("app/config.json", "r") as file:
    shops = json.load(file)["shops"]

shop_list = []

for shop in shops:
    shop_list.append(
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
    )
