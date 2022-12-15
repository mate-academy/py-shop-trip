from __future__ import annotations

import datetime


class Shops:
    shops_list = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def add_shop(shops: list) -> list[Shops]:
        shops_list = []
        for shop in shops:
            new_shop = Shops(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            shops_list.append(new_shop)
        return shops_list

    @staticmethod
    def customer_purchase(
            customer_name: str,
            purchase_note: dict
    ) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        print(f"{purchase_note['milk']}")
        print(f"{purchase_note['bread']}")
        print(f"{purchase_note['butter']}")
        print(f"Total cost is {purchase_note['total']} dollars")
        print("See you again!\n")
