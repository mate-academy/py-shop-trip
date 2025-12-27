import datetime
from typing import Any


class Shop:
    def __init__(self, shops: dict) -> None:
        self.name = shops["name"]
        self.location = shops["location"]
        self.products = shops["products"]

    def shopping_bill(self, customer: Any) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, quantity in customer.product_cart.items():
            price = quantity * self.products[product]
            print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {customer.product_price(self).get(self.name)}"
              f" dollars")
        print("See you again!\n")
