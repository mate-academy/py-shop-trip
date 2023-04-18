from dataclasses import dataclass
from typing import List


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def calculate_purchase(self, product_cart: dict) -> float:
        result = []
        for product, amount in product_cart.items():
            result.append(amount * self.products[product])
        return sum(result)
