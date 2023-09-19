from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int, int]
    products: dict[str: int | float]
