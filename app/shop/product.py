from dataclasses import dataclass
from typing import Union, Self


@dataclass
class Product:
    name: str
    price: Union[int, float]

    @classmethod
    def from_dict(cls, product: dict) -> Self:
        return cls(name=product["name"], price=product["price"])
