from __future__ import annotations
import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return f"{self.name}"

    def print_check(
            self,
            customer_name: str,
            product_cart: dict,
    ) -> None:
        now = datetime.datetime.now()
        print(now.strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, quantity in product_cart.items():

            if product in self.products:
                summary = quantity * self.products[product]
                print(f"{quantity} {product}s for "
                      f"{self.convert_to_int(summary)} dollars")
                total += summary
        print(f"Total cost is {total} dollars\n"
              f"See you again!\n")

    @classmethod
    def from_dict(cls, shop: dict) -> Shop:
        return cls(
            shop.get("name"),
            shop["location"],
            shop.get("products")
        )

    @staticmethod
    def convert_to_int(value: float) -> int | float:
        if value == int(value):
            return int(value)
        return value
