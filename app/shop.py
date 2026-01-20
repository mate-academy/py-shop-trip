from __future__ import annotations
import datetime


class Customer:
    pass


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name,
        self.location = location
        self.products = products

    def print_receipt(self, customer: Customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
              f"\nThanks, {customer.name}, for your purchase!\n"
              "You have bought: ")
        total_product = 0
        for product in customer.product_cart:
            count_product = customer.product_cart.get(product)
            cost_product = self.products.get(product, 0)
            cost_type_product = cost_product * count_product
            if int(cost_type_product) == cost_type_product:
                cost_type_product = int(cost_type_product)
            total_product += cost_type_product
            print(f"{count_product} {product}s for "
                  f"{cost_type_product} dollars")
        print(f"Total cost is {total_product} dollars\n"
              "See you again!")
