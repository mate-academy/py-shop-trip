from dataclasses import dataclass
from typing import List
from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def get_cost_food(self, customer: Customer) -> float:
        cost_food = 0
        for food in customer.product_cart.keys():
            cost_food += customer.product_cart[food] * self.products[food]
        return cost_food
