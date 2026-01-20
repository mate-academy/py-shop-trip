import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from app.car import Location

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = Location(location)
        self.products = products

    def calculate_purchase(self, customer: "Customer") -> Decimal:
        return Decimal(
            sum([
                Decimal(
                    str(quantity)
                ) * Decimal(
                    str(self.products[customer_product])
                )
                for customer_product, quantity in customer.product_cart.items()
            ]
            )
        )

    def fulfilled_purchase(self, customer: "Customer") -> str:
        receipt = (
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\nYou have bought"
        )
        receipt += ":\n"
        total_cost_str = (
            f"Total cost is "
            f"{self.calculate_purchase(customer)} dollars\n"
        )
        for customer_product, quantity in customer.product_cart.items():
            decimal_quantity = Decimal(str(quantity))
            decimal_shop_product_cost = Decimal(
                str(self.products[customer_product])
            )
            cost_for_products = decimal_quantity * decimal_shop_product_cost
            if cost_for_products % 1 == 0:
                cost_for_products = int(cost_for_products)
            receipt += (
                f"{quantity} {customer_product}s "
                f"for {cost_for_products} dollars\n"
            )
            customer.product_cart[customer_product] = 0
        receipt += total_cost_str + "See you again!\n"
        return receipt
