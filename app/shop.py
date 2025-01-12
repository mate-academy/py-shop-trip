import json
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.json")


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def define_shops() -> list:
    with open(config_file_path, "r") as file:
        data = json.load(file)
        shops = []
        for shop in data["shops"]:
            shops.append(Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            ))
    return shops
