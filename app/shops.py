import json
from pathlib import Path


class Shops:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def create_shops_objects():
    base_dir = Path(__file__).resolve().parent

    with open(base_dir / "config.json", "r") as file:
        data = json.load(file)
        shops = data["shops"]
        shops_list = []
        for shop in shops:
            shops_list.append(Shops(name=shop["name"],
                                    location=shop["location"],
                                    products=shop["products"]))
    return shops_list
