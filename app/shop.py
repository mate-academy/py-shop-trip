import math
from typing import List


class Shop:
    def __init__(self, name: str, location: List, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_purchase_cost(self, customer: object) -> float:
        total_cost = 0.0

        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_price = self.products[product]
                cost_for_product = product_price * quantity
                total_cost += cost_for_product

        return round(total_cost, 2)

    def print_receipt(self, customer: object) -> None:
        date = "04/01/2021 12:33:41"
        print(f"Date: {date}\nThanks, "
              f"{customer.name}, "
              f"for your purchase!\nYou have bought:")
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_price = self.products[product]
                cost_for_product = product_price * quantity
                cost_for_product_frac, cost_for_product_int \
                    = math.modf(cost_for_product)
                cost_for_product_after = cost_for_product_frac * 10
                if cost_for_product_after == 0:
                    cost_for_product = int(cost_for_product_int)
                print(f"{quantity} {product}s for {cost_for_product} dollars")
        total_cost = self.calculate_purchase_cost(customer)
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
