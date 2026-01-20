import datetime

from typing import Any


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

    def print_receipt(self, customer: Any) -> None:
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            cost = self.products[product] * quantity
            total_cost += cost
            print(
                f"{quantity} {product}s for "
                f"{cost if not cost.is_integer() else int(cost)} dollars"
            )
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()
