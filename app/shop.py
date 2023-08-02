from __future__ import annotations

import datetime
from typing import List


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_amount_for_products(self, product_cart: dict) -> int | float:
        total_amount = 0
        for product_name, count in product_cart.items():
            total_amount += self.products.get(product_name, 0) * count
        return total_amount

    def print_bill(self, product_cart: dict, name: str) -> float:

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {name}, for your purchase!\n"
              "You have bought: ")

        total_amount = 0
        for product_name, count in product_cart.items():
            amount = self.products.get(product_name, 0) * count
            total_amount += amount
            print(f"{count} {product_name}s for {round(amount, 2)} dollars")

        print(
            f"Total cost is {round(total_amount, 2)} dollars\n"
            f"See you again!\n"
        )

    @classmethod
    def create_shops(cls, shops: List) -> List[Shop]:
        return [cls(**shop) for shop in shops]
