from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: list

    @classmethod
    def get_shop_info(cls, shop: dict) -> Shop:
        return cls(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
