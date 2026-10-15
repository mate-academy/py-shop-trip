from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    products: dict
    location: list
    money: int
    car: dict
