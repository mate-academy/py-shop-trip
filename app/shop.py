import datetime
from typing import Any


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: Any) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product_name, quantity in customer.product_cart.items():
            item_price = self.products[product_name]
            item_total = item_price * quantity
            total += item_total

            product_name_plural = product_name + "s"

            if isinstance(item_total, float) and item_total.is_integer():
                item_total = int(item_total)

            print(
                f"{quantity} {product_name_plural} for {item_total} dollars"
            )

        if isinstance(total, float) and total.is_integer():
            total = int(total)

        print(f"Total cost is {total} dollars")
        print("See you again!")
