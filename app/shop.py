from dataclasses import dataclass
from typing import Dict, List
import datetime


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, float]

    def calculate_cart_price(self, cart: Dict[str, int]) -> float:
        total = 0.0
        for product, quantity in cart.items():
            total += quantity * self.products[product]
        return total

    def print_receipt(self, customer_name: str, cart: Dict[str, int]) -> None:
        print(
            "\nDate: "
            f"""{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}"""
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in cart.items():
            price = self.products[product] * quantity
            if price == int(price):
                price = int(price)
            print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {self.calculate_cart_price(cart)} dollars")
        print("See you again!")
