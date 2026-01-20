from __future__ import annotations
from typing import List


class Shop:
    def __init__(
            self,
            name: str,
            location: List[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def load_from_dict(cls, shop: dict) -> Shop:
        return cls(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
