from __future__ import annotations
import datetime
from typing import Callable


class Shop:
    def __init__(self, name: str, location: list, products: dict, ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def make_instance(cls, shop: dict) -> Shop:
        return cls(
            shop["name"],
            shop["location"],
            shop["products"]
        )

    def print_bill(self, customer: Callable) -> None:
        current_time = datetime.datetime.now()
        print("Date:", current_time.strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        products_cost = 0
        for product_item in customer.product_cart:
            product_cost = (customer.product_cart[product_item]
                            * self.products[product_item])
            print(f"{customer.product_cart[product_item]} "
                  f"{product_item}s for {product_cost} dollars")
            products_cost += product_cost
        print(f"Total cost is {products_cost} dollars")
        print("See you again!\n")
