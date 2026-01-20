from __future__ import annotations

import datetime

from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.customer import Customer


@dataclass()
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def from_dict(cls, data: dict) -> Shop:
        return cls(
            **{
                key: data[key]
                for key in cls.__annotations__ if key in data
            }
        )

    def purchase_receipt(self, customer: Customer) -> None:
        shopping_list = [
            f"{customer.product_cart[product]} {product}s for "
            f"""{
                customer.product_cart[product] * self.products[product]
                if customer.product_cart[product]
                * self.products[product] % 1 != 0
                else int(
                    customer.product_cart[product] * self.products[product]
                )
            } dollars\n"""
            for product in customer.product_cart
            if product in self.products
        ]

        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:\n"
            f"{''.join(shopping_list)}"
            f"""Total cost is {sum(
                [
                    self.products[product] * customer.product_cart[product]
                    for product in customer.product_cart
                    if product in self.products
                ]
            )} dollars\n"""
            "See you again!\n"
        )
