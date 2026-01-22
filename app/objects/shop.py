import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print("\nDate:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer_name}, for your purchase!")

        cart_total = 0
        print("You have bought:")
        for product, amount in product_cart.items():
            product_total = self.products[product] * amount
            if product_total == int(product_total):
                product_total = int(product_total)
            cart_total += product_total
            print(f"{amount} {product}s for "
                  f"{product_total} dollars")

        print(f"Total cost is {cart_total} dollars")
        print("See you again!\n")
