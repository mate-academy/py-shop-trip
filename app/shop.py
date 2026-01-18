from __future__ import annotations

import datetime

from app.customer import Customer


def convert_if_whole_number(value: int | float) -> int | float:
    if value == int(value):
        return int(value)
    else:
        return value


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict = None
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def check_cost_products(self, list_products: dict) -> int | float:
        return sum(
            self.products[product] * count
            for product, count in list_products.items()
        )

    def get_store_receipt(self, customer: Customer) -> str:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")

        store_receipt = f"Date: {formatted_datetime}\n"
        store_receipt += f"Thanks, {customer.name}, for your purchase!\n"
        store_receipt += "You have bought:\n"

        total = 0
        for product_name, product_count in customer.product_cart.items():
            price = product_count * self.products[product_name]
            price = convert_if_whole_number(price)
            total += price
            if product_count > 1:
                store_receipt += (f"{product_count} {product_name}s for "
                                  f"{price} dollars\n")
            else:
                store_receipt += (f"{product_count} {product_name} for "
                                  f"{price} dollars\n")

        store_receipt += f"Total cost is {total} dollars\nSee you again!\n"

        return store_receipt
