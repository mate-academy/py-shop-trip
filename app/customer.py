from __future__ import annotations

import math
import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def cost_of_trip(self, shop: Shop, car: Car) -> float:
        diff_x = self.location[0] - shop.location[0]
        diff_y = self.location[1] - shop.location[1]
        length = math.sqrt(diff_x ** 2 + diff_y ** 2)
        mul = car.fuel_consumption * car.fuel_price * 2
        cost_of_road = (length / 100) * mul
        cost_of_purchase = self.make_shopping(shop)
        return round(cost_of_road + cost_of_purchase, 2)

    def get_shop(self, shop: Shop, car: Car) -> None:
        print(f"{self.name}'s trip to the {shop.name} "
              f"costs {self.cost_of_trip(shop, car)}")

    def make_shopping(self, shop: Shop) -> float:
        return sum(
            shop.products[product] * amount
            for product, amount in self.product_cart.items()
        )

    def print_receipt(self, shop: Shop) -> None:
        total_cost = self.make_shopping(shop)
        date_now = datetime.datetime.now()
        formatted_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, amount in self.product_cart.items():
            cost = shop.products[product] * amount
            if cost == int(cost):
                print(f"{amount} {product}s for {int(cost)} dollars")
            else:
                print(f"{amount} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print("")
