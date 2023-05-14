import json

from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict


def create_shops(shops: list) -> list:
    list_of_shops = list()
    for shop in shops:
        shop_obj = Shop(*shop.values())
        list_of_shops.append(shop_obj)

    return list_of_shops


with open("app/config.json", "r") as file:
    data = json.load(file)["shops"]

shops_list = create_shops(data)
