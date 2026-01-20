import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def print_check(self, customer: any) -> None:
        print("Date:", datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0

        for product, amount in customer.product_cart.items():
            price = amount * self.products[product]
            print(f"{amount} {product}s for {price:g} dollars")
            total_cost += price

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
