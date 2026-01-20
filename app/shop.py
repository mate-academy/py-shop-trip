from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    @classmethod
    def shop_info(cls, shop: dict) -> Shop:
        return cls(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
