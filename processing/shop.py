"""
This module defines the Shop class, which represents a shop with a name,
location, and products.
It includes methods for formatting values and printing receipts for customer
purchases.

Classes:
    Shop: A class representing a shop with methods to format values and print
    receipts.

Methods:
    __init__(self, shop: dict) -> None:
        Initializes a Shop instance with the given shop details.

    format_value(value: float) -> str:
        Formats a float value to a string, removing trailing zeros and decimal
        points if necessary.

    print_receipt(self, customer_name: str, customer_products: dict) -> None:
        Prints a receipt for the given customer name and products purchased.
"""
from __future__ import annotations

import datetime


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop.get("name")
        self.location = shop.get("location")
        self.products = shop.get("products")

    @staticmethod
    def format_value(value: float) -> str:
        return str(value).rstrip("0").rstrip(".")

    def print_receipt(
            self,
            customer_name: str,
            customer_products: dict
    ) -> None:

        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = (f"Date: {date}\n"
                   f"Thanks, {customer_name}, for your purchase!\n"
                   "You have bought:\n")
        total_cost = 0
        for product, count in customer_products.items():
            price = count * self.products.get(product, 0)
            total_cost += price
            receipt += (
                f"{count} {product}s for "
                f"{self.format_value(price)} dollars\n"
            )
        receipt += (
            f"Total cost is "
            f"{self.format_value(total_cost)} dollars\n"
        )
        receipt += "See you again!\n"
        print(receipt)
