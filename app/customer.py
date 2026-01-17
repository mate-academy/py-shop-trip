
from dataclasses import dataclass


@dataclass
class Customers:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: dict
