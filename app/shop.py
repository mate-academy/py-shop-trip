from typing import Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def serve_the_customer(self, visitor: Any) -> bool:

        test_date = datetime(2021, 1, 4, 12, 33, 41)
        visiting_time = test_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {visiting_time}")
        print(f"Thanks, {visitor.name}, for your purchase!")
        print("You have bought: ")

        total_cost = 0
        for product, count in visitor.product_cart.items():
            if product in self.products:
                cost = self.products[product] * count
                total_cost += cost
                print(f"{count} {product} for {cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        return True
