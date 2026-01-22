import datetime
from typing import List, Dict


class Shop:
    def __init__(
        self,
        name: str,
        location: List[int],
        products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, cart: Dict[str, int]) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_products_cost = 0.0
        for product, quantity in cart.items():
            price = self.products[product]
            cost = price * quantity
            total_products_cost += cost
            unit = "milks" if product == "milk" else f"{product}s"
            print(f"{quantity} {unit} for {cost:.2f} dollars")
        print(f"Total cost is {total_products_cost:.2f} dollars")
        print("See you again!")
