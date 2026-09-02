import datetime
from typing import Any


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def print_receipt(self, customer: Any) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for key, value in customer.product_cart.items():
            price = value * self.products[key]
            if price == int(price):
                price = int(price)
            print(f"{value} {key}s for {price} dollars")

        print(f"Total cost is {customer.full_price_in_shop(self)} dollars")
        print("See you again!")
