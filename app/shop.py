import math

from app.customer import Customers
from app.unpack_file import open_file


class Shops:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def road_cost(self, customer: Customers) -> int:
        return round(
            (math.dist(self.location, customer.location) * 2)
            * (customer.car["fuel_consumption"] / 100)
            * open_file()["fuel_price"], 2
        )

    def total_price_products(self, customer: Customers) -> float:
        total_price_products = (
            (self.products["milk"] * customer.product_cart["milk"])
            + (self.products["bread"] * customer.product_cart["bread"])
            + (self.products["butter"] * customer.product_cart["butter"])
        )
        return total_price_products

    def total_price_trip(self, customer: Customers) -> float:
        print(
            f"{customer.name}'s trip to the {self.name} costs "
            f"{self.total_price_products(customer) + self.road_cost(customer)}"
        )
        return self.total_price_products(customer) + self.road_cost(customer)

    def purchase_receipt(self, customer: Customers) -> None:
        customer.location = self.location
        print(
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for you purchase!\n"
            f"You have bought: "
        )
        for product in customer.product_cart:
            print(
                f"{customer.product_cart[product]} {product}s for "
                f"{customer.product_cart[product] * self.products[product]}"
                f" dollars"
            )
        print(
            f"Total cost is {self.total_price_products(customer)} dollars\n"
            f"See you again!"
            f"\n"
        )

    def way_home(self, customer: Customers) -> None:
        for dict_customer in open_file()["customer_list"]:
            if customer.name == dict_customer["name"]:
                customer.location = dict_customer["location"]

        rest_of_money = (
            customer.money
            - self.total_price_products(customer)
            - self.road_cost(customer)
        )
        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now has {rest_of_money} dollars\n"
        )
