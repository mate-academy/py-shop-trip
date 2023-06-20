from dataclasses import dataclass
import datetime
from typing import Type


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def calculate_products_cost(
            self,
            product_cart: dict
    ) -> int | float:
        return sum(
            self.products[product] * count
            for product, count in product_cart.items()
        )

    def buy_products(self, customer: Type) -> str:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        purchase = (
            f"Date: {date}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: \n"
        )

        for product, count in customer.product_cart.items():
            purchase += (
                f"{count} {product}s for "
                f"{count * self.products[product]} dollars\n"
            )

        total_cost = self.calculate_products_cost(customer.product_cart)

        purchase += (
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n\n"
        )

        customer.money = round(customer.money - total_cost, 2)

        return purchase
