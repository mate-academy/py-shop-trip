import math
import datetime
from typing import Any


def _fmt_money(xar: float) -> str:
    return str(int(xar)) if float(xar).is_integer() else str(xar)


class Shop:
    def __init__(self, name: str, location: Any, products: dict) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = dict(products)

    def distance_to(self, other_location: Any) -> float:
        x1, y1 = self.location
        x2, y2 = other_location
        return math.hypot(y2 - y1, x2 - x1)

    def products_cost(self, cart: dict) -> float | None | Any:
        total = 0.0
        for prod, qty in cart.items():
            if prod not in self.products:
                return None
            total += self.products[prod] * qty
        return total

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        def fmt_money(xar: float) -> str:
            return str(int(xar)) if float(xar).is_integer() else str(xar)

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
            print(f"{qty} {prod}{'s' if qty > 1 else ''}"
                  f" for {fmt_money(cost)} dollars")

        print(f"Total cost is {fmt_money(total)} dollars")
        print("See you again!")
        print()
