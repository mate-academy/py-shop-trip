import datetime

from math import sqrt
from typing import List

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            customer_location: List[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.customer_location = customer_location
        self.money = money
        self.car = car

    def initial_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance(
            self,
            shop_location: list,
            fuel_consumption: float,
            fuel_price: float
    ) -> float:
        x1, y1 = self.customer_location
        x2, y2 = shop_location
        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        trip_to_shop = dist / 100 * fuel_consumption * fuel_price * 2

        return round(trip_to_shop, 2)

    def time_for_shopping(self, shop: Shop) -> None:
        total_cost = 0.0
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")

        product_price_list = [value for value in shop.products.values()]
        product_list = iter(product_price_list)

        for key, value in self.product_cart.items():
            cost = value * next(product_list)
            total_cost += cost
            print(f"{value} {key}s for {cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
