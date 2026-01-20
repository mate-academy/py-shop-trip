from dataclasses import dataclass
from typing import Dict


@dataclass
class Shop:
    name: str
    location: list[int, int]
    products: dict

    def calculate_total_cost(self, product_cart: Dict[str, int]) -> float:
        total_cost = sum(
            self.products[product] * quantity
            for product, quantity in product_cart.items()
            if product in self.products
        )
        return round(total_cost, 2)
