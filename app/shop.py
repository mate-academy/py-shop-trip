from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer

# required


class Shop:
    def __init__(
            self,
            shop: dict
    ) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def calculate_products_cost(self, customer_products: dict) -> int | float:
        return sum(
            customer_products[key] * value
            for key, value in self.products.items()
        )

    def receipt(self, customer: Customer) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0

        for product, quantity in customer.product_cart.items():
            cost = quantity * self.products[product]
            print(f"{quantity} {product}s for"
                  f" {int(cost) if isinstance(cost, float) and cost.is_integer() else cost} "
                  f"dollars")
            total_cost += cost

        print(f"Total cost is {total_cost} dollars")

        print("See you again!")
        print("")
