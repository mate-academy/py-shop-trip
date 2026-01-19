from __future__ import annotations
from typing import Any

from app.point import Point


class Shop:
    def __init__(
            self,
            name: str,
            location: Point,
            products: dict[str, float | int]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def create_shop(
            cls,
            shop_info: dict[str, str | list[int] | dict[str, (int | float)]]
    ) -> Shop:
        return cls(
            name=shop_info["name"],
            location=Point.create_from_location(shop_info["location"]),
            products=shop_info["products"]
        )

    def sell(self, customer: Any) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for name, amount in customer.product_cart.items():
            product_price = amount * self.products[name]
            if product_price % int(product_price) == 0:
                product_price = int(product_price)
            print(f"{amount} {name}s for {product_price} dollars")
        total_cost = sum(
            amount * self.products[name]
            for name, amount in customer.product_cart.items()
        )
        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")
