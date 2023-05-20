from __future__ import annotations
from app.json_reader import read_file
from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: dict

    @staticmethod
    def create_customers() -> list[Customer]:
        return [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"]
            )
            for customer in read_file()[0]["customers"]
        ]
