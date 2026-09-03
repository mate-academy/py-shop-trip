from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    money: int
    location: list[int]
    car: Car

