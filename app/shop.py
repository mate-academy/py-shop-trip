from __future__ import annotations

import datetime
from math import ceil


class Shop:
    def __init__(self,
                 name: str,
                 products: dict[str, float],
                 location: list[int]) -> None:
        self.name = name
        self.products = products
        self.location = location

    @classmethod
    def from_dict(cls, shop: dict) -> Shop:
        return cls(name=shop["name"],
                   products=shop["products"],
                   location=shop["location"])

    def is_in_stock(self, products: dict[str, float]) -> bool:
        return all(product in self.products.keys()
                   for product, count in products.items())

    def receipt(self,
                name: str,
                products: dict[str, float]) -> list[float, str]:
        total_cost = 0
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = f"\nDate: {date}\n"
        receipt += f"Thanks, {name}, for you purchase!\n"
        receipt += "You have bought: \n"

        for product, count in products.items():
            count = ceil(count)
            cost = count * self.products[product]
            receipt += f"{count} {product}s for {cost} dollars\n"
            total_cost += round(cost, 2)

        receipt += f"Total cost is {total_cost} dollars\n"
        receipt += "See you again!\n"

        return [total_cost, receipt]
