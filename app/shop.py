import datetime
from typing import Any


class Shop:
    shops = []

    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.shops.append(self)

    def calculates_cost_of_product_cart(
        self,
        customer: Any,
        printing: bool = False
    ) -> int | float:
        product_cart_cost = 0
        for product, amount in customer.product_cart.items():
            if product in self.products:
                cost_of_product = amount * (self.products[product])
                product_cart_cost += cost_of_product
                if printing:
                    print(f"{amount} {product}s for {cost_of_product} dollars")
        return product_cart_cost

    def shop_purchase_display(self, customer: Any) -> None:
        today = datetime.datetime.today()
        transaction_datetime = today.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {transaction_datetime}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        total_cost = self.calculates_cost_of_product_cart(
            customer, printing=True
        )
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
