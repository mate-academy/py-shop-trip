from math import sqrt
import datetime

from app.car import Car
from app.shops import Shops


class Customers:

    def __init__(self, name: str,
                 product_cart: dict,
                 customer_location: list[int],
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.customer_location = customer_location
        self.money = money
        self.car = car

    def initial_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance(self,
                 shop_location: list[int],
                 fuel_consumption: float,
                 fuel_price: float) -> float:
        x1, y1 = self.customer_location
        x2, y2 = shop_location
        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        trip_to_shop = dist / 100 * fuel_consumption * fuel_price * 2

        return round(trip_to_shop, 2)

    def shopping_time(self, shop: Shops) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        for product_name, amount in self.product_cart.items():
            if product_name in shop.products:
                cost_product = amount * shop.products[product_name]
                round_cost_name = (int(cost_product)
                                   if cost_product == int(cost_product)
                                   else cost_product)
                print(f"{amount} {product_name}s for "
                      f"{round_cost_name} dollars")

        total_cost = sum(
            amount * shop.products[product_name]
            for product_name, amount in self.product_cart.items()
        )

        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!\n")
