from __future__ import annotations
from dataclasses import dataclass
from app.car import Location


@dataclass
class Shop:
    name: str
    location: Location
    products: dict

    def __repr__(self) -> str:
        return self.name
