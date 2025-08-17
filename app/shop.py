from datetime import datetime
from typing import Dict, Tuple


class Shop:
    def __init__(
            self, name: str, location: Tuple[int, int],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def sell(self, product: str, quantity: int) -> float:
        if product not in self.products:
            print(f"{product} is not available in {self.name}")
            return 0.0

        price = self.products[product]
        cost = price * quantity
        print(f"{quantity} {product}s for {cost:.1f} dollars")
        return cost

    def checkout(self, cart: Dict[str, int]) -> float:
        total = 0.0
        for product, quantity in cart.items():
            total += self.sell(product, quantity)
        print(f"Total cost is {total:.1f} dollars")
        return total

    def print_receipt(self) -> None:
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
