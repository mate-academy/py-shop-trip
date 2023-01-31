from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.customer import Customer

import datetime
import dataclasses


@dataclasses.dataclass
class Shop:
    shop_name: str
    shop_location: list[int]
    shop_prices: dict[str, float]

    @staticmethod
    def create_shop(shops: dict) -> list[Shop]:
        shop_list = []
        for shop in shops:
            shop_list.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"]
                )
            )
        return shop_list

    @staticmethod
    def starting_and_ending_of_function(func: callable) -> callable:
        def handler(shop: Shop, customer: Customer) -> callable:
            print(
                f"Date: "
                f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            )
            print(f"Thanks, {customer.name}, for you purchase!")
            func(shop, customer)
            print("See you again!\n")

        return handler

    @starting_and_ending_of_function
    def sell_products(self, customer: Customer) -> None:
        print("You have bought: ")
        total_cost = 0
        for product in customer.product_cart:
            product_cost = \
                customer.product_cart[product] * self.shop_prices[product]
            total_cost += product_cost
            customer.money -= product_cost
            print(f"{customer.product_cart[product]} {product}s "
                  f"for {product_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
