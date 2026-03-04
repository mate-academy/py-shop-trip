import datetime
from typing import Dict


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(
        self,
        customer_name: str,
        product_cart: Dict[str, int]
    ) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.isoformat()}")
        print(f"Thank you, {customer_name}!")
        total = 0
        for product, count in product_cart.items():
            if product in self.products:
                price = self.products[product] * count
                total += price
                print(f"{count} {product}s: ${price:.2f}")
        print(f"Total cost is ${total:.2f}")
        print("See you again!")
