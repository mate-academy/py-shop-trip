from typing import Dict, Tuple, Callable
from decimal import Decimal
from datetime import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: Tuple[int, int],
        products: Dict[str, Decimal]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, cart: Dict[str, int]) -> Decimal:
        return sum(
            self.products[product] * quantity
            for product, quantity in cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        cart: Dict[str, int],
        fmt_min: Callable[[Decimal], str]
    ) -> None:
        print(f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = Decimal("0")
        for product, quantity in cart.items():
            price
