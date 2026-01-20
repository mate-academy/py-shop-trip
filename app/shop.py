from __future__ import annotations
from dataclasses import dataclass
import datetime

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def get_name(self) -> str:
        return self.name

    def get_location(self) -> list:
        return self.location

    def get_products(self) -> dict:
        return self.products

    def shop_print_receipt(self, customer: Customer) -> None:
        milk_cost = self.get_products()["milk"] \
            * customer.get_product_cart()["milk"]
        bread_cost = self.get_products()["bread"] \
            * customer.get_product_cart()["bread"]
        butter_cost = self.get_products()["butter"] \
            * customer.get_product_cart()["butter"]

        current_date = datetime.datetime.now()

        print(
            f"Date: {current_date.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.get_name()}, for you purchase!\n"
            "You have bought: \n"
            f"{customer.get_product_cart()['milk']} "
            f"milks for {milk_cost} dollars\n"
            f"{customer.get_product_cart()['bread']} "
            f"breads for {bread_cost} dollars\n"
            f"{customer.get_product_cart()['butter']} "
            f"butters for {butter_cost} dollars\n"
            f"Total cost is {milk_cost + bread_cost + butter_cost} dollars\n"
            "See you again!\n"
        )
