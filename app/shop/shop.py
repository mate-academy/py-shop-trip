import datetime
from typing import List

from app.products.products import Products


class Shop:
    def __init__(
            self,
            name: str,
            location: List[int],
            products: List[Products],
    ):
        self.name = name
        self.location = location
        self.products = products

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: List[int]):
        self._location = location

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products: List[Products]):
        self._products = products

    def buy_from_customer(self, customer):
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        all_products = customer.calculate_product(self)
        counter = 0

        for name, amount in customer.product_cart.items():
            print(f"{amount} {name}s for {all_products[counter]} dollars")
            counter += 1

        print(f"Total cost is {all_products[-1]} dollars")
        print("See you again!\n")
