from __future__ import annotations

import datetime
from dataclasses import dataclass
from math import ceil


@dataclass
class Shop:
    name: str
    products: dict[str, float]
    location: list[int]

    @classmethod
    def from_dict(cls, shop: dict) -> Shop:
        return cls(name=shop["name"],
                   products=shop["products"],
                   location=shop["location"])

    def is_in_stock(self, products: dict[str, int]) -> bool:
        return all([product in self.products.keys()
                    for product, count in products.items()])

    def check(self,
              name: str,
              products: dict[str, float]) -> list[float, str]:
        total_cost = 0
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        check = f"\nDate: {date}\n"
        check += f"Thanks, {name}, for you purchase!\n"
        check += "You have bought: \n"
        for product, count in products.items():
            count = ceil(count)
            cost = count * self.products[product]
            check += f"{count} {product}s for {cost} dollars\n"
            total_cost += round(cost, 2)
        check += f"Total cost is {total_cost} dollars\n"
        check += "See you again!\n"
        return [total_cost, check]
