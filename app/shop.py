from __future__ import annotations
from typing import List


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def create_shops(shops_data: dict) -> List[Shop]:
        shops_json = shops_data["shops"]
        shops = [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in shops_json
        ]
        return shops

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
