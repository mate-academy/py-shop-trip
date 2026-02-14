import datetime
import math
from typing import Any, Optional


def format_money(amount: float) -> str:
    amount = float(amount)
    if amount.is_integer():
        return str(int(amount))
    return str(amount)


class Shop:
    def __init__(self, name: str, location: Any, products: dict) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = dict(products)

    def distance_to(self, other_location: Any) -> float:
        x1, y1 = self.location
        x2, y2 = other_location
        return math.hypot(x2 - x1, y2 - y1)

    def products_cost(self, cart: dict) -> Optional[float]:
        total_cost = 0.0
        for product_name, quantity in cart.items():
            if product_name not in self.products:
                return None
            total_cost += self.products[product_name] * quantity
        return total_cost

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0
        for product_name, quantity in cart.items():
            price = self.products[product_name]
            cost = quantity * price
            total_cost += cost

            suffix = "s" if quantity > 1 else ""
            print(
                f"{quantity} {product_name}{suffix} "
                f"for {format_money(cost)} dollars"
            )

        print(f"Total cost is {format_money(total_cost)} dollars")
        print("See you again!")
        print()
