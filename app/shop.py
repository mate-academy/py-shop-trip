from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict
