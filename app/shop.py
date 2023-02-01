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

    @products_price.setter
    def products_price(self, products: dict) -> None:
        if not isinstance(products, dict):
            raise TypeError("Products should be dictionary")
        for product, price in products.items():
            if not isinstance(product, str):
                raise TypeError("Products names should be string values")
            elif not isinstance(price, (int, float)):
                raise TypeError("Products prices should be numeric")
            elif price < 0:
                raise ValueError("Products prices can't be negative")
        self.__products = products

    @property
    def location(self) -> list[int]:
        return self.__location

    @location.setter
    def location(self, location: list[int]) -> None:
        if not isinstance(location, list):
            raise TypeError("Location should be a list")
        for coordinate in location:
            if not isinstance(coordinate, int):
                raise TypeError("Coordinates should be integer")
        self.__location = location

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name should be string")
        self.__name = name

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
