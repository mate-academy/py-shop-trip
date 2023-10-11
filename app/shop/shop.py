import datetime
from typing import Dict, Any

from app.customer.customer import Customer


class Shop:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def sell_products(self, customer: Customer) -> None:
        print(
            f"\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        )
        print(f"Thanks, {customer.name}, for your purchase!\n")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            product_cost = quantity * self.products[product]
            print(
                f"You have bought: {quantity} {product}s "
                f"for {product_cost} dollars\n"
            )
            total_cost += product_cost
        print(f"Total cost is {total_cost} dollars\n")
        print("See you again!\n")
