from typing import Any
import json
import datetime
from dataclasses import dataclass


@dataclass()
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def create_shop(cls, file_name: str) -> list:
        with open(file_name, "r") as f_json:
            info = json.load(f_json)
            lst_shop = []
            for shop in info["shops"]:
                lst_shop.append(cls(name=shop["name"],
                                    location=shop["location"],
                                    products=shop["products"]))
            return lst_shop

    def print_bill(self, other: Any) -> None:
        now = datetime.datetime.now()
        total_result = 0
        print("Date:", now.strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {other.name}, for you purchase!")
        print("You have bought: ")
        for product, count in other.product_cart.items():
            result = other.product_cart[product] * self.products[product]
            total_result += result
            print(f"{count} {product}s for {result} dollars")
        print(f"Total cost is {total_result} dollars")
        print("See you again!\n")
