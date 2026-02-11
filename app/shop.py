from __future__ import annotations
import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


def _fmt_money(value: int | float) -> str:
    value_f = float(value)
    if value_f.is_integer():
        return str(int(value_f))
    return f"{value_f:.2f}".rstrip("0").rstrip(".")


@dataclass
class Shop:
    name: str
    location: tuple[int, int]
    products: dict[str, int | float]

    def customer_bill(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        total_purchase_cost = 0
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.products_to_buy.items():
            one_product_price = self.products[product] * quantity
            print(
                f"{quantity} {product}s for "
                f"{_fmt_money(one_product_price)} dollars"
            )
            total_purchase_cost += one_product_price
        print(f"Total cost is {_fmt_money(total_purchase_cost)} dollars")
        customer.money -= total_purchase_cost
        print("See you again!")
