from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.customer import Customer


class Shop:

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_bill(self, customer: "Customer") -> None:
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        total_price = 0
        print("You have bought:")
        for product_name, quantity in customer.product_cart.items():
            total_price += self.products[product_name] * quantity
            price = quantity * self.products[product_name]
            if price == int(price):
                price = int(price)
            print(f"{quantity} {product_name}s for {price} dollars")
        print(f"Total cost is {round(total_price, 2)} dollars")
        print("See you again!")
