from __future__ import annotations
import datetime


class Shop:
    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def cost_of_products(self, cart: dict) -> float:
        return sum(cart[product] * self.products[product] for product in cart)

    def print_receipt(self, name: str, product_cart: dict) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for position in product_cart:
            cost = product_cart[position] * self.products[position]
            print(f"{product_cart[position]} "
                  f"{position}s for {cost} dollars")
        print(f"Total cost is {self.cost_of_products(product_cart)} "
              f"dollars")
        print("See you again!\n")
