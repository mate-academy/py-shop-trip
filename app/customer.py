from dataclasses import dataclass
from typing import Dict, List

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[int]
    money: float
    car: Car
