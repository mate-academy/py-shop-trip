from dataclasses import dataclass
from typing import List
from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def get_cost_food(self, customer: Customer) -> float:
        return sum(
            count * self.products[food]
            for food, count in customer.product_cart.items()
        )
