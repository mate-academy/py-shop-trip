from __future__ import annotations
from typing import Any
import datetime


def format_money(money: int | float, char: int) -> int | float:
    return int(money) if money == int(money) else round(money, char)


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def price(self, product: str, count_of_product: int) -> float | int:
        return self.products[product] * count_of_product

    def total_price(self, customer: Any) -> float | int:
        return sum(
            self.price(product, count)
            for product, count in customer.product_cart.items()
        )

    def purchase_receipt(self, customer: Any) -> None:
        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, count in customer.product_cart.items():
            print(f"{count} {product}s for "
                  f"{format_money(self.price(product, count), 1)} dollars")
        print(f"Total cost is "
              f"{format_money(self.total_price(customer), 2)} dollars")
        print("See you again!\n")
