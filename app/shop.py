from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def products_cost(self, cart: dict) -> dict:
        return {
            product: cart[product] * self.products[product]
            for product in cart
        }

    def shopping(self, customer_name: str, cart: dict) -> None:
        print("Date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        products_cost = self.products_cost(cart)
        for product in products_cost:
            print(f"{cart[product]} {product}s for "
                  f"{self.round_price(products_cost[product])} dollars")

        print(f"Total cost is {sum(self.products_cost(cart).values())}"
              f" dollars")
        print("See you again!\n")

    @staticmethod
    def round_price(price: float) -> int | float:
        if int(price) == price:
            return int(price)
        return price
