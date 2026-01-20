from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    products_cart: dict
    location: list
    money: int
