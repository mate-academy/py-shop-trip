from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict


def create_shop(shop_data: Dict) -> Shop:
    return Shop(
        shop_data["name"],
        shop_data["location"],
        shop_data["products"]
    )
