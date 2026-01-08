from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, float]

    def cost_of_products(self, product_cart: Dict[str, int]) -> float:
        total = 0.0
        for product, qty in product_cart.items():
            if product not in self.products:
                return None
            total += self.products[product] * qty
        return total

    def has_all_products(self, product_cart: Dict[str, int]) -> bool:
        return all(product in self.products for product in product_cart)
