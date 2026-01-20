from __future__ import annotations
from typing import Any


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_dict(cls, dictionary: dict) -> Shop:
        return cls(
            dictionary["name"],
            dictionary["location"],
            dictionary["products"]
        )

    def calculate_cart_cost(self, cart: dict) -> float:
        return sum(
            self.products[product] * quantity
            for product, quantity in cart.items()
        )

    def process_purchase(self, customer: Any) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in customer.product_cart.items():
            cost = self.products[product] * quantity
            if int(cost) == cost:
                cost = int(cost)
            print(f"{quantity} {product}s for {round(cost, 1)} dollars")
            total_cost += cost

        print(f"Total cost is {round(total_cost, 2)} dollars")
        customer.money -= total_cost
        print("See you again!\n")
