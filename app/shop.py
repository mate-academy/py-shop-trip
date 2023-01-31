from __future__ import annotations
import datetime

import app.customer as cust


class Shop:
    shops = {}

    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.__name = name
        self.__location = location
        self.__products = products
        Shop.shops[self.__name] = self

    @property
    def products_price(self) -> dict:
        return self.__products

    @property
    def location(self) -> list[int]:
        return self.__location

    @property
    def name(self) -> str:
        return self.__name

    def print_receipt(self, customer: cust.Customer) -> None:
        today = datetime.datetime.now()
        date_string = today.strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {date_string}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, price in self.products_price.items():
            amount = customer.product_cart.get(product)
            cost = amount * price
            total_cost += cost
            print(f"{amount} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
