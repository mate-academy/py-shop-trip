from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.utils import format_amount

if TYPE_CHECKING:
    from app.customer import Customer


@dataclass(slots=True)
class Shop:
    name: str
    location: list[int]
    products: dict[str, float]

    @classmethod
    def from_dict(cls, shop_data: dict) -> Shop:
        return cls(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"],
        )

    def has_products(self, product_cart: dict[str, int]) -> bool:
        return all(product in self.products for product in product_cart)

    def calculate_products_cost(self, product_cart: dict[str, int]) -> float:
        return sum(
            self.products[product] * count
            for product, count in product_cart.items()
        )

    def create_receipt(self, customer: Customer) -> str:
        total_cost = self.calculate_products_cost(customer.product_cart)

        lines = [
            f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}",
            f"Thanks, {customer.name}, for your purchase!",
            "You have bought:",
        ]
        for product, amount in customer.product_cart.items():
            price = self.products[product] * amount
            lines.append(
                f"{amount} {product}s for {format_amount(price)} dollars"
            )
        lines.append(f"Total cost is {format_amount(total_cost)} dollars")
        lines.append("See you again!")
        return "\n".join(lines)
