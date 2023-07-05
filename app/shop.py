from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List
import datetime


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, int]

    def print_receipt(self, customer: Customer) -> None:
        customer.money -= customer.chosen_shop.shopping_cost
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for product in customer.product_cart:
            print(f"{customer.product_cart[product]} {product}s for "
                  f"{customer.product_cart[product] * self.products[product]} "
                  f"dollars")
        print(f"Total cost is {customer.chosen_shop.shopping_cost} dollars")
        print("See you again!\n")
