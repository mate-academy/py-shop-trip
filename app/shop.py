import datetime
from typing import Any


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shopping_bill(self, customer: Any) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product, quantity in customer.product_cart.items():
            price = self.products[product] * quantity
            print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is "
              f"{customer.product_price(self).get(self.name)} dollars")
        print("See you again!\n")
