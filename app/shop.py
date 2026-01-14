from __future__ import annotations
from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def create_shops_list(cls, shops: list[dict]) -> list[Shop]:
        shops_list = []
        for shop in shops:
            shops_list.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"]
                )
            )
        return shops_list

    def calculate_cart_cost(self, customers_cart: dict) -> dict:
        return {
            product: round(self.products[product] * customers_cart[product], 1)
            for product in customers_cart.keys()
        }

    def print_receipt(self, cart: dict, customer_name: str) -> float:
        recipt_date = datetime.datetime.strftime(
            datetime.datetime.now(),
            "%d/%m/%Y %H:%M:%S"
        )
        cost = self.calculate_cart_cost(cart)
        total = sum(cost.values())
        print(f"Date: {recipt_date}")
        print(f"Thanks, {customer_name}, for your purchase!\nYou have bought:")
        for product in cart:
            print(f"{cart[product]:g} milks for {cost[product]:g} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!")
        return total
