from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: [int, int]
    products: dict
