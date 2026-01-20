from __future__ import annotations
from app.customer import Customer


class Shop:
    def __init__(
            self,
            shop: dict
    ) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def products_cost(
            self,
            product_cart: dict
    ) -> float:
        return sum(
            self.products[product] * amount
            for product, amount in product_cart.items()
        )

    def bill_info(
            self,
            customer: Customer
    ) -> None:
        date = "04/01/2021 12:33:41"
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in customer.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{self.products[product] * amount} dollars")

        print(f"Total cost is "
              f"{self.products_cost(customer.product_cart)} dollars")
        print("See you again!\n")
