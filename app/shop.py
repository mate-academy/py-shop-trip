from dataclasses import dataclass
from typing import Dict, List

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, float | int]

    def get_product_cost(self, customer: Customer) -> float | int:
        return sum(quantity * self.products.get(product_id)
                   for product_id, quantity in customer.product_cart.items()
                   )
