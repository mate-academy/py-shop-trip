from __future__ import annotations
from app.data_jason import load_json
import dataclasses
from typing import List


@dataclasses.dataclass
class Store:
    name: str
    location: List[int]
    products: dict

    @classmethod
    def get_stores(cls) -> list[Store]:
        data = load_json(filename="app/config.json")

        stores = [
            cls(
                name=data_store["name"],
                location=data_store["location"],
                products=data_store["products"]
            )
            for data_store in data["shops"]
        ]

        return stores
