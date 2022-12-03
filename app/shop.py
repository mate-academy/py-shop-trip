from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.customer import Customer

"""
TYPE_CHECKING from the "typing" module has been imported
and the "if TYPE_CHECKING" condition has been implemented
to provide for type annotations for the "customer" parameter
of the "products_price" and "print_purchase_receipt" methods
without cyclic imports
"""


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_price(self, customer: Customer) -> float:
        total_price = 0
        for product, number in customer.product_cart.items():
            total_price += self.products[product] * number
        return total_price

    def print_purchase_receipt(self, customer: Customer) -> None:
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}\nThanks, {customer.name}, "
              f"for you purchase!\nYou have bought: ")
        for product, price in self.products.items():
            print(f"{customer.product_cart[product]} {product}s for "
                  f"{customer.product_cart[product] * price} dollars")
        print(f"Total cost is {self.products_price(customer)} "
              f"dollars\nSee you again!\n")
