from __future__ import annotations

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

    def print_receipt(self, customer: Customer) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        total_cost = 0
        for key, value in customer.product_cart.items():
            product_cost = self.products[key] * value

            if product_cost == int(product_cost):
                product_cost = int(product_cost)

            print(f"{value} {key}s for {product_cost} dollars")
            total_cost += self.products[key] * value

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
