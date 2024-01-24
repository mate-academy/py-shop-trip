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

    def make_shopping_proces(self, customer: Any) -> None:
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:"
        )
        total = 0
        for product, quantity in customer.product_cart.items():
            cost = quantity * self.products[product]
            cost = int(cost) if cost == int(cost) else cost
            total += cost
            print(f"{quantity} {product}s for " f"{cost} dollars")

        print(f"Total cost is {total} dollars\nSee you again!\n")
