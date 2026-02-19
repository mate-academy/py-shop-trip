from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import Dict

from .utils import Location, money_trim


@dataclass(frozen=True)
class Shop:
    """Shop with a location and a price list for products."""

    name: str
    location: Location
    products: Dict[str, float]

    def can_fulfill_cart(self, cart: Dict[str, int]) -> bool:
        """Return True if the shop has all products from cart."""
        return all(product_name in self.products for product_name in cart)

    def cart_cost(self, cart: Dict[str, int]) -> float:
        """Calculate total cost of the cart in this shop."""
        total_cost = 0.0
        for product_name, quantity in cart.items():
            unit_price = float(self.products[product_name])
            total_cost += quantity * unit_price
        return total_cost

    def print_receipt(self, customer_name: str, cart: Dict[str, int]) -> None:
        """Print purchase receipt using current datetime."""
        now_value = datetime.datetime.now()

        # Test expects: 04/01/2021 12:33:41 for Jan 4, 2021 -> DD/MM/YYYY
        now_str = now_value.strftime("%d/%m/%Y %H:%M:%S")

        print("\nDate:", now_str)
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0
        for product_name, quantity in cart.items():
            unit_price = float(self.products[product_name])
            item_total = quantity * unit_price
            total_cost += item_total

            plural_name = f"{product_name}s"
            print(
                f"{quantity} {plural_name} for "
                f"{money_trim(item_total)} dollars"
            )

        print(f"Total cost is {money_trim(total_cost)} dollars")
        print("See you again!\n")
