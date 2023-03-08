from app.customer import Customer
from datetime import datetime


def unpack_shops(data: list) -> list:
    list_shops = []
    for shop in data:
        list_shops.append(Shop(shop))
    return list_shops


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.products = shop["products"]
        self.location = shop["location"]

    def recipe(self, customer: Customer) -> None:
        total_price = 0
        dt = datetime(2021, 4, 1, 12, 33, 41)
        datetime_recipe = dt.strftime("%m/%d/%Y %H:%M:%S")
        print(
            f"Date: {datetime_recipe}\nThanks, "
            f"{customer.name}, for you purchase!\nYou have bought: "
        )
        for name, value in customer.product_cart.items():
            print(f"{value} {name}s for {value * self.products[name]} dollars")
            total_price += value * self.products[name]
        print(f"Total cost is {total_price} dollars\nSee you again!\n")
