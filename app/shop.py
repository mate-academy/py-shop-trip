import datetime

from typing import Any


def fmt(num: float) -> float | int:
    rounded = round(num, 2)
    return int(rounded) if rounded == int(rounded) else rounded


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def calculate_products_cost(self, cart: dict) -> float:
        return sum(
            self.products[item] * amount for item, amount in cart.items()
        )

    def print_receipt(self, customer: Any) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0
        for item, amount in customer.product_cart.items():
            cost = self.products[item] * amount
            total += cost
            print(f"{amount} {item}s for {fmt(cost)} dollars")

        print(f"Total cost is {fmt(total)} dollars")
        print("See you again!")
