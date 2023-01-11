import json
from datetime import datetime

# import app.customers as cust


class Shops:

    def __init__(
            self,
            name: str,
            location: str,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def create_shops_list() -> list:
        with open("app/config.json") as config:
            info = json.load(config)

        shops_ls = []

        for shop in info["shops"]:
            new_shop = Shops(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            shops_ls.append(new_shop)
        return shops_ls

    def shopping(self, customer: object) -> None:
        date = datetime(2021, 1, 4, 12, 33, 41)
        print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")
        total_price = 0
        for item in customer.product_cart:
            total_item_price = customer.product_cart[item] * self.products[item]
            total_price += total_item_price
            print(f"{customer.product_cart[item]} {item}s for {total_item_price}"
                  f" dollars")
        print(f"Total cost is {total_price} dollars\n"
              f"See you again!\n"
              f"\n{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n"
              )
