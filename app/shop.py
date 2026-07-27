from __future__ import annotations
import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase_receipt(self, customer: "Customer") -> None:  # noqa: F821
        customer.location = self.location
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, value in customer.product_cart.items():
            product_total_cost_ = value * self.products.get(product)
            product_total_cost = (
                int(product_total_cost_)
                if int(product_total_cost_) == float(product_total_cost_)
                else float(product_total_cost_)
            )
            print(f"{value} {product}s for {product_total_cost} dollars")
            total_cost += product_total_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
