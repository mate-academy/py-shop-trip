from datetime import datetime
from typing import Dict

from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def serve_customer(self, customer: Customer) -> Dict[str, dict]:
        sold_products = {}

        for product in customer.product_cart:
            amount = customer.product_cart[product]
            cost = customer.product_cart[product] * self.products[product]

            cost = int(cost) if cost == int(cost) else cost

            sold_products[product] = {"amount": amount, "cost": cost}
        return sold_products

    def print_purchase_receipt(self, customer: Customer) -> None:
        current_date = datetime(2021, 1, 4, 12, 33, 41)
        current_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

        sold_products = self.serve_customer(customer)
        total_cost = 0

        print(f"Date: {current_date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought: ")

        for product, data in sold_products.items():
            total_cost += data["cost"]
            print(f"{data['amount']} {product}s for {data['cost']} dollars")

        print(f"Total cost is {round(total_cost, 2)} dollars\n"
              "See you again!"
              "\n")
