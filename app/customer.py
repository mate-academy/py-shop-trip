from dataclasses import dataclass
from typing import List

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: Car
