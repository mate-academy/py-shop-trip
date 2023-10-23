import datetime
from typing import List
import dataclasses

from app.customer import Customer


@dataclasses
class Shop:
    name: str
    location: List[int]
    products: dict

    def serve_customer(self, customer: Customer) -> str:
        total = 0
        
        for product, quantity in customer.product_cart.items():
            pass
        
        print(
            f"Date: {datetime.now()}"
            f"Thanks, {customer.name} for your purchase!"
            "You have bought:\n"
            f"{customer.product_cart}"
        )