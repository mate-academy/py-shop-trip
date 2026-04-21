import datetime
from typing import Dict
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(
        self,
        customer: Customer,
        products: Dict[str, int],
        products_cost: float,
    ) -> None:
        date_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date_str}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for name, qty in products.items():
            price = self.products[name]
            print(f"{qty} {name}s for {(price * qty):g} dollars")

        print(f"Total cost is {products_cost:g} dollars")
        print("See you again!")
