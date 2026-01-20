from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: Decimal
    car: Car
