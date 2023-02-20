from __future__ import annotations

from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def print_customers_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")
