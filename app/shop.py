import datetime
from typing import Any


class Shop:
    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.location = info["location"]
        self.products = info["products"]

    def products_purchase(self, customer: Any) -> None:
        today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {today}")
        customer.location = self.location
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        spent_money = 0
        for name, count in customer.product_cart.items():
            if name in self.products:
                cost = self.products[name] * count
                spent_money += cost
                print(f"{count} {name}s for {cost} dollars")

        print(f"Total cost is {spent_money} dollars\nSee you again!\n")
