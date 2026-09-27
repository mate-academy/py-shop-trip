from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    @classmethod
    def from_dict(cls, data: dict) -> Shop:
        """Factory method for Shop class"""
        return cls(
            name=data["name"],
            location=data["location"],
            products=data["products"]
        )

    def get_product_cost(self, product: str, number: int) -> float | int:
        cost = self.products[product] * number
        return int(cost) if cost == int(cost) else cost

    def format_receipt_item(self, product: str, number: int) -> str:
        """Format receipt item with product name and number"""
        item_name = product if number == 1 else f"{product}s"
        item_total = self.get_product_cost(product, number)
        return f"{number} {item_name} for {item_total} dollars"

    def print_receipt(self, customer: Customer) -> None:
        """Create receipt with customer items and prices"""
        date_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        items_lines = [
            self.format_receipt_item(product, number)
            for product, number in customer.product_cart.items()
        ]

        total_price = customer.cart_price(self.products)
        if total_price == int(total_price):
            total_price = int(total_price)

        receipt_text = (
            f"Date: {date_now}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:\n"
            + "\n".join(items_lines) + "\n"
            f"Total cost is {customer.cart_price(self.products)} dollars\n"
            f"See you again!"
        )

        print(receipt_text)
