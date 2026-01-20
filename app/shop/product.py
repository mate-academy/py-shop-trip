from __future__ import annotations
from dataclasses import dataclass
from typing import Union


@dataclass
class Product:
    name: str
    price: Union[int, float]

    @classmethod
    def from_dict(cls, product: dict) -> Product:
        return Product(name=product["name"], price=product["price"])
