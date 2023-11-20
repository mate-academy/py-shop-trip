from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, float | int]

    def get_product_cost(self, customer: Customer) -> float | int:
        return sum(value * self.products.get(key)
                   for key, value in customer.product_cart.items())
