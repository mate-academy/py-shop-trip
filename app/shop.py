from dataclasses import dataclass
from typing import List
from app.load_from_file import get_dict_from_json_file


@dataclass
class Shop:
    name: str
    location: List
    products: dict


def create_shops() -> List[Shop]:
    shops = get_dict_from_json_file()["shops"]
    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in shops
    ]
