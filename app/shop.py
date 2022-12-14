from __future__ import annotations
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
        self, name: str, location: list[int, int], products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return self.name

    def serve_customer(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, amount in customer.product_cart.items():
            total_cost += self.products[product] * amount
            print(
                f"{amount} {product}s for"
                f" {self.products[product] * amount} dollars"
            )
        print(f"Total cost is {total_cost} dollars")
        customer.money -= total_cost
        print("See you again!\n")
