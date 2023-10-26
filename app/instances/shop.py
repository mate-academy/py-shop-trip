from dataclasses import dataclass
import datetime
from typing import List

from app.instances.customer import Customer


@dataclass
class Shop:

    name: str
    location: List[int]
    products: dict

    def serve_customer(self, customer: Customer) -> None:
        total = 0

        receipt = (
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            f"\nThanks, {customer.name}, for your purchase!\n"
            "You have bought: \n"
        )

        for product, quantity in customer.product_cart.items():
            cost = self.products[product] * quantity

            if isinstance(cost, float) and cost % 1 == 0:
                cost = int(cost)
            receipt += f"{quantity} {product}s for {cost} dollars\n"
            total += cost

        receipt += f"Total cost is {total} dollars\nSee you again!\n"

        if customer.money > total:
            customer.money -= total
        else:
            print("You don't have enough money\n")

        print(receipt)
