from __future__ import annotations
import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Shop:
    name: str
    location: List[int | float]
    products: dict

    def buying_product(self, customer: "Customer") -> int | float:
        customer.location = self.location

        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought: ")
        total_cost = 0
        for product, amount in customer.products.items():
            cost = amount * self.products.get(product, 0)
            print(f"{amount} {product}s for {cost} dollars")
            total_cost += cost

        customer.money = round(customer.money - total_cost, 2)
        total_cost = round(total_cost, 2)
        print(
            f"Total cost is {total_cost} dollars\n"
            "See you again!\n"
        )
        return total_cost
