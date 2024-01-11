# from datetime import datetime
from app.customer import Customer
import math


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance_to_customer(self, customer: Customer) -> float:
        return math.dist(self.location, customer.location)

    def calculate_purchase_cost(self, customer: Customer) -> int | float:
        return sum(quantity * customer.product_cart[item]
                   for item, quantity in self.products.items())

    def print_rides_to_shop(self, customer: Customer) -> None:
        print(f"{customer.name} rides to {self.name}\n")

    @staticmethod
    def round_num(num: int | float) -> int | float:

        float_num = float(round(num, 2))

        return int(float_num) if float_num.is_integer() else float_num

    def print_receipt(self, customer: Customer) -> None:
        total_amount = 0
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought: ")
        for item, quantity in customer.product_cart.items():
            cost = quantity * self.products[item]
            total_amount += cost
            print(f"{quantity} {item}s for {self.round_num(cost)} dollars")
        print(f"Total cost is {total_amount} dollars\n"
              f"See you again!\n")
