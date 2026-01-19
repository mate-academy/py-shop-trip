from __future__ import annotations
import datetime


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop.get("name")
        self.location = shop.get("location")
        self.products = shop.get("products")

    @staticmethod
    def format_value(value: float) -> str:
        return str(value).rstrip("0").rstrip(".")

    def print_receipt(
            self,
            customer_name: str,
            customer_products: dict
    ) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = ""
        receipt += f"Date: {date}\n"
        receipt += f"Thanks, {customer_name}, for your purchase!\n"
        receipt += "You have bought:\n"
        total_cost = 0
        for product, count in customer_products.items():
            price = count * self.products.get(product, 0)
            total_cost += price
            receipt += (
                f"{count} {product}s for "
                f"{self.format_value(price)} dollars\n"
            )
        receipt += (
            f"Total cost is "
            f"{self.format_value(total_cost)} dollars\n"
        )
        receipt += "See you again!\n"
        print(receipt)
