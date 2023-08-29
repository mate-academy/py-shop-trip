import json

import datetime

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart(self, cart: dict) -> int:
        price = 0
        for name, product_price in self.products.items():
            if name in cart:
                price += product_price * cart[name]

        return price

    def purchase(self, customer: Customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        total_price = 0
        for name, count in customer.product_cart.items():
            product_cost = self.products[name] * count
            print(f"{count} {name}s for {product_cost} dollars")
            total_price += product_cost

        print(f"Total cost is {total_price} dollars\n" f"See you again!\n")


def load_shops(file_data: json) -> list:
    shops = []

    for shop in file_data["shops"]:
        shop = Shop(shop["name"], shop["location"], shop["products"])
        shops.append(shop)

    return shops
