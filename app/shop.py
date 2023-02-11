from dataclasses import dataclass


@dataclass()
class Shops:
    name: str
    location: list[int]
    products: dict
