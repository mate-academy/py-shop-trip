from __future__ import annotations
from dataclasses import dataclass
import datetime
from decimal import Decimal

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Shop) -> bool:
        return all(
            (
                self.name == other.name,
                self.location == other.location,
                self.products == other.products,
            )
        )

    def sell(self, customer: Customer) -> None:
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(
            f"Date: {timestamp}\nThanks, {customer.name}"
            f", for your purchase!\nYou have bought:"  # noqa: E231
        )
        total_product_spent = Decimal(0)
        for product in customer.product_cart:
            product_spent = Decimal(customer.product_cart[product]) * Decimal(
                f"{self.products[product]}"
            )
            print(
                f"{customer.product_cart[product]} "
                f"{product}s for "
                f"{float(round(product_spent, 2)):g} dollars"  # noqa: E231
            )
            total_product_spent += product_spent
            total_product_spent_str = str(round(
                total_product_spent, 2
            )).rstrip("0").rstrip(".")
        print(f"Total cost is {total_product_spent_str} "
              f"dollars\nSee you again!")
        print()
