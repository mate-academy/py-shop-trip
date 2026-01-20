import datetime
from typing import Any


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shopping(self, customer: Any) -> None:
        print("")
        actual_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {actual_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            product_cost = quantity * self.products[product]
            if isinstance(product_cost, float) and product_cost % 1 == 0:
                product_cost = int(product_cost)
            print(f"{quantity} {product}s for {product_cost} dollars")
            total_cost += product_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print("")
