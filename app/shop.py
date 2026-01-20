from datetime import datetime
from typing import Any


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def format_price(price: float) -> str:
        return f"{price: .2f}".rstrip("0").rstrip(".")

    def print_receipt(self, customer: Any) -> None:
        purchase_time = datetime(
            2021, 4, 1, 12, 33, 41
        ).strftime("%m/%d/%Y %H:%M:%S")
        total_cost = customer.calculate_cost_of_product_cart(self)
        print(f"\nDate: {purchase_time}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought:")
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                print(f"{quantity} {product}s for"
                      f"{(self.format_price(product_cost))} dollars")
        print(f"Total cost is {total_cost} dollars\n"
              "See you again!\n")
