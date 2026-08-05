import datetime
from math import sqrt
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car

    @staticmethod
    def distance_trip(customers_location: list, shop_location: list) -> float | int :
        return sqrt((customers_location[0] - shop_location[0]) ** 2 + (customers_location[1] - shop_location[1]) ** 2)

    def total_cost_of_products(self, shop: dict) -> float | int :
        total_cost_of_products = 0
        for key, item in self.product_cart.items():
            total_cost_of_products += self.product_cart[key] * shop[key]
        return total_cost_of_products

    def print_receipt(self, shop: Shop) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            cost = quantity * shop.products[product]
            print(f"{self.product_cart[product]} {product}s for {self.format_price(cost)} dollars")
        print(f"Total cost is {self.format_price(self.total_cost_of_products(shop.products))} dollars")
        print("See you again!\n")

    @staticmethod
    def format_price(price: int | float) -> str | int :
        return f"{price:.10f}".rstrip("0").rstrip(".")
