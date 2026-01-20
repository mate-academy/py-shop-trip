# app/shop.py

from datetime import datetime
from typing import Dict, List


class Shop:
    def __init__(self, name: str, location: List[float],
                 products: Dict[str, float]) -> None:
        """
        Initialize a Shop instance.

        :param name: The name of the shop.
        :param location: The shop's location as a list of coordinates [x, y].
        :param products: A dictionary of products and their prices.
        """
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: "Customer") -> None:
        """Print the purchase receipt for the customer."""
        current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            cost = self.products.get(product, 0) * quantity
            total_cost += cost
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
