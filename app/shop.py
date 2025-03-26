from __future__ import annotations
import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cashiers_check(self, customer: "Customer") -> None:  # noqa: F821
        customer.location = self.location
        date_now = datetime.datetime.now()
        print(f"Date: {date_now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, value in customer.product_cart.items():
            products_cost = value * self.products[product]
            products_cost = (
                int(products_cost)
                if int(products_cost) == float(products_cost)
                else float(products_cost)
            )
            print(f"{value} {product}s for {products_cost} dollars")
            total_cost += products_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
