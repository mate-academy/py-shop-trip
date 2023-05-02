import json
import datetime
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def receipt(self, customer: Customer) -> int:
        date_today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_today}"
              f"\nThanks, {customer.name}, for your purchase!"
              f"\nYou have bought: ")
        total = 0
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                sum_product = quantity * self.products[product]
                total += sum_product
                print(
                    f"{quantity} "
                    f"{product if quantity == 1 else product + 's'} "
                    f"for {sum_product} dollars")
        return total


with open("app/config.json", "r") as file_json:
    shops = json.load(file_json)["shops"]

shops_list = [Shop(shop["name"],
                   shop["location"],
                   shop["products"])
              for shop in shops]
