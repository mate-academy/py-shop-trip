from __future__ import annotations

import datetime
from typing import List

from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: List[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, customer: Customer) -> float | int:
        cust_product_list = customer.product_cart
        total_cost_products = 0
        for product, numbers in cust_product_list.items():
            if product in self.products:
                total_cost_products += self.products[product] * numbers

        return total_cost_products

    def receipt(self, customer: Customer) -> None:
        now_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cust_list = customer.product_cart
        all_products = self.calculate_products_cost(customer)
        print(f"Date: {now_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for title, number in cust_list.items():
            total_price_elem = self.products[title] * number
            if total_price_elem == int(total_price_elem):
                total_price_elem = int(total_price_elem)
            print(f"{number} {title}s for {total_price_elem} dollars")
        print(f"Total cost is {all_products} dollars")
        print("See you again!\n")
