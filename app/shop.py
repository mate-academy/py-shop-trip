import json
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict


with open("app/config.json", "r") as file:
    shops = json.load(file)["shops"]

shop_list = [
    Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    )
    for shop in shops
]
