import datetime

from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def print_check(self, customer: any) -> None:
        print("Date:", datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in customer.product_cart.items():
            price = amount * self.products[product]
            print(f"{amount} {product}s for {price} dollars")

        print(f"Total cost is {customer.product_price(self).get(self.name)}"
              f" dollars")
        print("See you again!")
