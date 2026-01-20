import datetime
from unittest import mock

from app.customer import Customer
from app.point import Point


class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = Point(shop_data["location"])
        self.products = shop_data["products"]

    def calculate_shopping(self, customer: Customer) -> float:
        total_price = 0
        for item in customer.product_cart.keys():
            total_price += self.products[item] * customer.product_cart[item]
        return total_price

    def make_shopping(self, customer: Customer) -> None:
        total_cost = 0
        with mock.patch("datetime.date") as datetime_mock:
            datetime_mock.return_value = datetime.datetime(
                2021,
                1,
                4,
                12,
                33,
                41)

            print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for item in customer.product_cart.keys():
            amount = customer.product_cart[item]
            position_price = self.products[item] * amount
            total_cost += position_price
            price_str = "{:g}".format(float(position_price))
            print(f"{amount} {item}s for {price_str} dollars")
        customer.money -= total_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
