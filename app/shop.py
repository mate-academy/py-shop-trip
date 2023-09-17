from typing import Dict, Any
from datetime import datetime


class Shop:
    def __init__(self, info: Dict[str, Any]) -> None:
        self.name = info["name"]
        self.location = info["location"]
        self.products = info["products"]

    def sell_products(self, customer) -> None:
        total_cost = 0
        receipt_products = []

        for product, quantity in customer.product_cart.items():
            if product in self.products:
                cost = quantity * self.products[product]
                total_cost += cost
                receipt_products.append(f"{quantity} {product}s "
                                        f"for {cost} dollars")

        print(f"\nDate: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for receipt_product in receipt_products:
            print(receipt_product)

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

        customer.money -= total_cost
