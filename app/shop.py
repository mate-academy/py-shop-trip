from __future__ import annotations
import json
import datetime
from typing import Any


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def count_price(self,
                    product: str,
                    number_of_pieces: int | float
                    ) -> int | float:
        price = self.products[product] * number_of_pieces
        if isinstance(price, float) and price.is_integer():
            return int(price)
        return price

    def sell_products(self, customer: Any) -> None:
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product in customer.product_cart:
            try:
                price_per_products = self.count_price(
                    product, customer.product_cart[product])
                total_cost += price_per_products
                print(f"{customer.product_cart[product]} "
                      f"{product}s for {price_per_products} dollars")
            except KeyError:
                print(f"Unfortunately, there is no {product} in {self.name}")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")


def create_shops_list() -> list:
    with open("app\\config.json", "r") as file:
        file_dict = json.load(file)
        shops_file_list = file_dict["shops"]
    shops_list = []
    for shop in shops_file_list:
        shops_list.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))
    return shops_list
