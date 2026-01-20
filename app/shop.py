from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
from decimal import Decimal
from dataclasses import dataclass

if TYPE_CHECKING:
    from .customer import Customer


def _decimal_to_str(value: Decimal) -> str:
    if value == int(value):
        return str(int(value))
    return str(value).rstrip("0")


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, Decimal]

    @classmethod
    def from_dict(cls, dict_: dict) -> Shop:
        return cls(
            name=dict_["name"],
            location=dict_["location"],
            products={
                k: Decimal.from_float(v) for k, v in dict_["products"].items()
            },
        )

    def get_products_costs(
        self, products: dict[str, int]
    ) -> dict[str, Decimal]:
        try:
            return {
                product: self.products[product] * quantity
                for product, quantity in products.items()
            }
        except KeyError as e:
            raise NoProductException(e.args[0]) from e

    def serve_customer(self, customer: Customer) -> None:
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        costs = self.get_products_costs(customer.product_cart)
        for product, cost in costs.items():
            print(
                f"{customer.product_cart[product]} {product}s"
                f" for {_decimal_to_str(round(cost, 2))} dollars"
            )

        total_cost = round(sum(costs.values()), 2)
        print(f"Total cost is {_decimal_to_str(total_cost)} dollars")
        customer.money -= total_cost
        customer.product_cart.clear()
        print("See you again!")


class NoProductException(Exception):
    """This exception occurs when requested product is not in the shop"""
