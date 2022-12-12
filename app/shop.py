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
        total_milk = other.product_cart["milk"] * self.products["milk"]
        total_bread = other.product_cart["bread"] * self.products["bread"]
        total_butter = other.product_cart["butter"] * self.products["butter"]
        total_product = total_milk + total_bread + total_butter
        print("Date:", now.strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {other.name}, for you purchase!")
        print("You have bought: ")
        print(f"{other.product_cart['milk']} milks for {total_milk} dollars")
        print(f"{other.product_cart['bread']} "
              f"breads for {total_bread} dollars")
        print(f"{other.product_cart['butter']} "
              f"butters for {total_butter} dollars")
        print(f"Total cost is {total_product} dollars")
        print("See you again!")
