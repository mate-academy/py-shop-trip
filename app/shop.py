from __future__ import annotations
import dataclasses
import datetime

from app.customer import Customer


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    def shop_print_receipt(self, customer: Customer) -> None:
        milk_cost = self.products["milk"] \
            * customer.product_cart["milk"]
        bread_cost = self.products["bread"] \
            * customer.product_cart["bread"]
        butter_cost = self.products["butter"] \
            * customer.product_cart["butter"]

        current_date = datetime.datetime.now()

        print(f"Date: {current_date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        print(f"{customer.product_cart['milk']} "
              f"milks for {milk_cost} dollars")
        print(f"{customer.product_cart['bread']} "
              f"breads for {bread_cost} dollars")
        print(f"{customer.product_cart['butter']} "
              f"butters for {butter_cost} dollars")
        print(f"Total cost is {milk_cost + bread_cost+butter_cost} dollars")
        print("See you again!\n")
