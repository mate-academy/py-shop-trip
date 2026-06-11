import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_purchase_receipt(self, customer: Customer) -> str:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = (f"Date: {now}\n"
                   f"Thanks, {customer.name}, for your purchase!\n"
                   f"You have bought:\n")
        total_cost = 0.
        for product_name, quantity in customer.products.items():
            product_cost = round(quantity * self.products[product_name], 2)
            total_cost += product_cost
            receipt += (f"{quantity} {product_name}s "
                        f"for {product_cost:g} dollars\n")

        receipt += (f"Total cost is {total_cost} dollars\n"
                    f"See you again!\n")
        return receipt
