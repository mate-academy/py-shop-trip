from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_product_cost(self, product: int, quantity: int) -> dict:
        price_of_product = quantity * self.products[product]
        return price_of_product
