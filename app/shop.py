import datetime
from typing import Any


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: Any) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for item, quantity in customer.product_cart.items():
            if item in self.products and self.products[item] > 0:
                item_cost = customer.product_cart[item] * self.products[item]
                print(f"{quantity} {item}s for {item_cost} dollars")
                total_cost += item_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
