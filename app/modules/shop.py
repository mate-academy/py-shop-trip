from typing import TypedDict


class Product(TypedDict):
    milk: float
    bread: float
    butter: float


class Shop(TypedDict):
    name: str
    location: list[float]
    products: Product
