from datetime import datetime
from typing import Dict, List


class Shop:
    def __init__(self,
                 name: str,
                 location: List[float],
                 products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: Dict[str, int]) -> float:
        total_cost = 0.0
        for product, quantity in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
        return total_cost

    def print_receipt(self,
                      customer_name: str,
                      product_cart: Dict[str, int],
                      total_cost: float) -> None:
        fixed_datetime = datetime(2021, 4, 1, 12, 33, 41)
        print(f"Date: {fixed_datetime.strftime("%m/%d/%Y %H:%M:%S")}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            if product in self.products:
                price = self.products[product] * quantity
                if price == int(price):  # Check if the price is a whole number
                    price = int(price)
                print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
