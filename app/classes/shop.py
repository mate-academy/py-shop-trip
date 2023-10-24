from __future__ import annotations
from datetime import datetime

from app.classes.from_dict import FromDict
from app.classes.customer import Customer


class Shop(FromDict):
    def __init__(self,
                 name: str = "",
                 location: list = None,
                 products: dict = None) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def from_dict(cls_dict: dict) -> Shop:
        new_shop = Shop()
        for key in cls_dict:
            setattr(new_shop, key, cls_dict[key])
        return new_shop

    def print_receipt(self, customer: Customer) -> float:
        timestamp = datetime.strftime(
            datetime.now(),
            "%d/%m/%y %H:%M:%S"
        )
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for key, value in customer.product_cart.items():
            print(f"{value} {key}s for {self.products[key]} dollars")
            total_cost += self.products[key]
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

        return total_cost
