from dataclasses import dataclass
import json
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def get_receipt(self, customer: object, car: object) -> None:
        date = datetime(2021, 1, 4, 12, 33, 41)
        timestamp = date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, amount in customer.product_cart.items():
            price = amount * self.products[product]
            print(f"{amount} {product}s for {price} dollars")
        products_price = customer.trip_costs(self, car)[0]
        print(f"Total cost is {products_price} dollars")
        print("See you again!\n")


def to_class() -> list:
    result = []
    with open("app/config.json", "r") as source:
        data = json.load(source)
        for shop in data["shops"]:
            shop = Shop(shop["name"], shop["location"], shop["products"])
            result.append(shop)
        return result


shop_list = to_class()
