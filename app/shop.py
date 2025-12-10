import copy
from dataclasses import dataclass
from typing import Any

import app.point as point
from app.purchase import Purchase


@dataclass
class Shop:
    name: str
    location: point.Point
    products: dict[str, int]

    def calculate_shopping(self, customer: Any) -> dict:
        test_customer = copy.deepcopy(customer)
        customer_cart = []
        total_cost = 0

        for product, quantity in test_customer.product_cart.items():
            if product in self.products:
                product_cost = 0
                product_number = 0

                while quantity > 0:
                    product_cost += self.products[product]
                    quantity -= 1
                    product_number += 1

                customer_cart.append(
                    Purchase(product, product_number, product_cost)
                )
                total_cost += product_cost

        return {
            "cart": customer_cart,
            "shopping_cost": total_cost,
        }
