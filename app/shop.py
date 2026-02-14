import datetime
import math
from typing import Any, Optional


def fmt_money(x: float) -> str:
    """Return '3' instead of '3.0', keep '12.5' as '12.5'."""
    x = float(x)
    if x.is_integer():
        return str(int(x))
    return str(x)


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
        total = 0.0
        for prod, qty in cart.items():
            if prod not in self.products:
                return None
            total += self.products[prod] * qty
        return total

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total = 0.0
        for prod, qty in cart.items():
            price = self.products[prod]
            cost = qty * price
            total += cost
            suffix = "s" if qty > 1 else ""
            print(f"{qty} {prod}{suffix} for {fmt_money(cost)} dollars")

        print(f"Total cost is {fmt_money(total)} dollars")
        print("See you again!")
        print()
