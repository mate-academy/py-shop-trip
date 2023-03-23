from typing import List
from datetime import datetime


class Shop:

    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def buy_products(self, customer_name: str,
                     customer_product_cart: dict) -> None:

        total_products_cost = 0
        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date}")
        print(f"Thanks, {customer_name}, for your purchase!")

        print("You have bought: ")
        for product_name, product_price in self.products.items():
            product_cost = (customer_product_cart[product_name]) * (
                self.products[product_name])
            print(f"{customer_product_cart[product_name]} {product_name}s "
                  f"for {product_cost} dollars")
            total_products_cost += product_cost

        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!\n")
