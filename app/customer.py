from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    wanted_products: dict
    location: list[int]
    money: int
    car: Car
