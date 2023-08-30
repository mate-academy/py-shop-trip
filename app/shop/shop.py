import datetime
from typing import List, Self

from app.customer.customer import Customer
from app.customer.product_cart import ProductCart


class Shop:
    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_price_for_cart(self, cart: ProductCart) -> float:
        price = 0
        for name, number in cart.product_list.items():
            if name in self.products:
                price += self.products[name] * number

        return round(price, 2)

    def purchase(self, customer: Customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        total_price = 0
        cart = customer.product_cart.product_list
        for name, number in cart.items():
            if name in self.products:
                price = self.products[name] * number
                total_price += price
                print(f"{number} {name}s for {price} dollars")

        print(f"Total cost is {total_price} dollars\n" f"See you again!\n")

    @classmethod
    def from_dict(cls, shop: dict) -> Self:
        return cls(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
