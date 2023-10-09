import math
import datetime

from dataclasses import dataclass
from typing import List
from app.customer import Customer


def format_num(num: int | float) -> int | float:
    float_num = float(round(num, 2))
    return int(float_num) if float_num.is_integer() else float_num


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def distance(self, customer: Customer) -> float:
        return math.dist(self.location, customer.location)

    def ride_to_shop(self, customer: Customer) -> None:
        print(f"{customer.name} rides to {self.name}\n")

    def products_cost(self, customer: Customer) -> int | float:
        return sum(self.products[prod] * customer.product_cart[prod]
                   for prod in self.products.keys())

    def print_receipt(self, customer: Customer) -> None:
        total = 0
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for prod, quantity in customer.product_cart.items():
            price = quantity * self.products[prod]
            total += price
            print(f"{quantity} {prod}s for {format_num(price)} dollars")
        print(f"Total cost is {total} dollars\n"
              f"See you again!\n")
