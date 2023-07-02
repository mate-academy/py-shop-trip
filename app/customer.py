from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict[str]
    location: list[int]
    money: int
    car: dict[str]
