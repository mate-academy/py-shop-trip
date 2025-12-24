from __future__ import annotations
import datetime


class Shop:
    def __init__(self, name : str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_price(self, product_cart: dict) -> float:
        return sum(self.products[prod] * qty
                   for prod, qty in product_cart.items())

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {dt_string}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, qty in product_cart.items():
            price = self.products[product] * qty
            for_price = int(price) if price == int(price) else price
            print(f"{qty} {product}s for {for_price} dollars")
        print(f"Total cost"
              f" is {self.calculate_cart_price(product_cart)} dollars")
        print("See you again!\n")
