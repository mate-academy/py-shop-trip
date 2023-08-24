import dataclasses
from typing import Dict
from decimal import Decimal
from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    products: Dict[str, int]
    location: list[int]
    money: Decimal
    car: Car
