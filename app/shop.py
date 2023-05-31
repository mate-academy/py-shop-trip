from __future__ import annotations
from dataclasses import dataclass
from app.car import Location


@dataclass
class Shop:
    name: str
    location: Location
    products: list[Product]

    def __repr__(self) -> str:
        return self.name


@dataclass
class Product:
    name: str
    price: int | float = None
    quantity: int = None

    def __repr__(self) -> str:
        return self.name
