from __future__ import annotations

import datetime
from typing import Dict, Tuple, TYPE_CHECKING

from app.utils import format_money

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: Tuple[float, float],
        products: Dict[str, float],
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = products

    def cart_cost(self, cart: Dict[str, int]) -> float:
        total = 0
        for item, amount in cart.items():
            total += self.products[item] * amount
        return total

    def print_receipt(self, customer: "Customer") -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0
        for item, amount in customer.product_cart.items():
            price = self.products[item]
            cost = price * amount
            total += cost
            print(f"{amount} {item}s for {format_money(cost)} dollars")

        print(f"Total cost is {format_money(total)} dollars")
        print("See you again!")
