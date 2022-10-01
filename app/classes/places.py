from __future__ import annotations
import datetime
import math


class Shop:
    def __init__(
        self, name: str, location: list[int], products: dict[int]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, cart: dict[int]) -> None:
        current_time = datetime.datetime.now().strftime(
            "Date: %d/%m/20%y %H:%M:%S\n"
        )
        purchase_formatted = []
        purchase_cost = 0

        for product, amount in cart.items():
            cost = amount * self.products[product]
            purchase_formatted.append(
                f"{amount} {product}s for {cost} dollars\n"
            )

            purchase_cost += cost

        print(
            current_time,
            f"Thanks, {customer_name}, for you purchase!\n",
            "You have bought: \n",
            *purchase_formatted,
            f"Total cost is {purchase_cost} dollars\n",
            "See you again!\n",
            sep="",
        )
