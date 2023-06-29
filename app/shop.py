from __future__ import annotations

import datetime


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_dict(cls, shop_info: dict) -> Shop:
        return cls(shop_info["name"],
                   shop_info["location"],
                   shop_info["products"])

    def print_check(self,
                    customer_name: str,
                    customer_product_cart: dict) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              "You have bought: ")
        total_cost = 0
        for key, value in customer_product_cart.items():
            total_cost += round(self.products[key] * value, 2)
            print(f"{value} {key}s for "
                  f"{round(self.products[key] * value, 2)} dollars")
        print(f"Total cost is {total_cost} dollars\n"
              "See you again!\n")
