from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from app.constants import RECEIPT_DATETIME_FORMAT
from app.utils import format_money

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: tuple[int, int],
        products: dict[str, float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def handle_purchase(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime(RECEIPT_DATETIME_FORMAT)}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in customer.product_cart.items():
            price = self.products[product]
            cost = round(price * quantity, 2)
            total_cost += cost
            print(
                f"{quantity} {product}s for {format_money(cost)} dollars"
            )

        total_cost = round(total_cost, 2)
        print(f"Total cost is {format_money(total_cost)} dollars")
        print("See you again!\n")
