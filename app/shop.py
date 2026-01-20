from __future__ import annotations
import dataclasses
from datetime import datetime
from decimal import Decimal

from app.customer import Customer


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_prices_for_products(
            self, customer_prod_cart: dict
    ) -> list[Decimal]:
        prices = []
        for product, amount in customer_prod_cart.items():
            product_price = Decimal(str(self.products[product]))
            product_total_sum = amount * product_price

            if product_total_sum == product_total_sum.to_integral_value():
                product_total_sum = int(product_total_sum)

            prices.append(product_total_sum)

        return prices

    def get_receipt(self, customer: Customer) -> str:
        receipt_datetime = datetime(
            2021, 1, 4, 12, 33, 41
        ).strftime("%d/%m/%Y %H:%M:%S")

        receipt = (
            f"\nDate: {receipt_datetime}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:\n"
        )

        prices = self.calculate_prices_for_products(customer.product_cart)

        for i, (product, amount) in enumerate(customer.product_cart.items()):
            product_total_sum = prices[i]

            receipt += (
                f"{amount} {product}s "
                f"for {product_total_sum} dollars\n"
            )

        total_cost = sum(prices)
        receipt += f"Total cost is {total_cost} dollars\nSee you again!\n"

        return receipt

    @staticmethod
    def from_dict(shop_dict: dict) -> Shop:
        return Shop(
            shop_dict["name"],
            shop_dict["location"],
            shop_dict["products"]
        )
