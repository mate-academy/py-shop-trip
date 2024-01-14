import datetime
from dataclasses import dataclass
import json


@dataclass
class Shop:
    name: str
    location: list[int]
    products_list: dict

    def has_in_stock(self, item: str) -> bool:
        return self.products_list.get(item)

    def calculate_cart_cost(self, product_cart: dict) -> float:
        total = 0

        for product, quantity in product_cart.items():
            product_price = quantity * self.products_list[product]
            total += product_price

        return total

    def get_receipt(
            self,
            customer_name: str,
            product_cart: dict
    ) -> None:
        current_date = datetime.datetime.now()
        current_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {current_date}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")

        for product, quantity in product_cart.items():
            product_price = quantity * self.products_list[product]
            print(f"{quantity} {product}s for {product_price} dollars")

        total = self.calculate_cart_cost(product_cart)
        print(f"Total cost is {total} dollars")
        print("See you again!\n")


def load_shops_from_json(file_name: str) -> list[Shop]:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        shops = data["shops"]
        return [
            Shop(
                shop["name"],
                shop["location"],
                shop["products"],
            )
            for shop in shops
        ]
