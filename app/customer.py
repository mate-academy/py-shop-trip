from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: Decimal
    car: dict
