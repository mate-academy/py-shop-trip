from __future__ import annotations
import dataclasses
import datetime

import app.trip.customer as cust


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    @staticmethod
    def get_timestamp() -> str:
        current = datetime.datetime.now()
        return f"Date: {current.strftime('%d/%m/%Y %H:%M:%S')}"

    def give_receipt(self, customer: cust.Customer) -> None:
        print(f"\n{self.get_timestamp()}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, amount in customer.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{amount * self.products[product]} dollars")
        print(f"Total cost is "
              f"{customer.calculate_products_cost(self)} dollars")
        print("See you again!\n")

    @classmethod
    def from_dict(cls, dict_: dict) -> Shop:
        return Shop(
            dict_.get("name"),
            dict_.get("location"),
            dict_.get("products")
        )
