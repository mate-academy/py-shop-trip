from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.customer import Customer
import datetime


class Shop:

    def __init__(self, name: str, location: list[float],
                 products_and_prices: dict) -> None:
        self.name = name
        self.location = location
        self.products_and_prices = products_and_prices

    def check_if_has_products(self, product_cart: dict) -> bool:
        return all(product in self.products_and_prices
                   for product in product_cart)

    def calculate_price_of_products(self, product_cart: dict) -> float:
        return sum(quantity * self.products_and_prices[product]
                   for product, quantity in product_cart.items())

    def print_receipt(self, customer: Customer, product_cart: dict) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, quantity in product_cart.items():
            unit_price = self.products_and_prices[product]
            product_total = quantity * unit_price
            total += product_total
            print(
                f"{quantity} {product}s for "
                f"{product_total:g} dollars"
            )
        print(f"Total cost is {total:g} dollars")
        print("See you again!")
