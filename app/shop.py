from __future__ import annotations
from dataclasses import dataclass


@dataclass()
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def shop_object(cls, shops: list) -> list[Shop]:
        return [
            Shop(
                name=shop.get("name"),
                location=shop.get("location"),
                products=shop.get("products")
            ) for shop in shops
        ]
