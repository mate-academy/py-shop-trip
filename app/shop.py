import datetime

from app.customer import Customer
from app.location import Location
from app.product import Product


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = Location(*location)
        self.products = Product(**products)

    def buy(self, customer: Customer) -> None:
        print(f"{customer.name} rides to {self.name}\n")
        print("Date:",
              datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        print(f"{customer.product_cart.milk} milks for "
              f"{customer.product_cart.price_for_milks(
                  self.products)} dollars")
        print(f"{customer.product_cart.bread} breads for "
              f"{customer.product_cart.price_for_breads(
                  self.products)} dollars")
        print(f"{customer.product_cart.butter} butters for "
              f"{customer.product_cart.price_for_butters(
                  self.products)} dollars")
        print(f"Total cost is "
              f"{customer.shop_lowest_product_price} dollars")
        print("See you again!\n")
