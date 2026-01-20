from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, Decimal]


def return_shops(shops: list[dict]) -> list[Shop]:
    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ) for shop in shops
    ]
