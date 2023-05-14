import json

from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict


def create_shops(shops: list) -> list:
    list_of_shops = [Shop(*shop.values()) for shop in shops]

    return list_of_shops


with open("app/config.json", "r") as file:
    data = json.load(file)["shops"]

shops_list = create_shops(data)
