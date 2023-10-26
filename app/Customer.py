from math import sqrt
import datetime

from app.Shop import Shop
from app.Car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 customer_location: list,
                 money: int,
                 car: Car
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.customer_location = customer_location
        self.money = money
        self.car = car

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance(self,
                 shop_location: list,
                 fuel_consumption: float,
                 fuel_price: float) -> float:
        customer_x, customer_y = self.customer_location
        shop_x, shop_y = shop_location
        distance = sqrt((shop_x - customer_x) ** 2
                        + (shop_y - customer_y) ** 2)
        shop_trip = distance / 100 * fuel_consumption * fuel_price * 2

        return round(shop_trip, 2)

    def shopping(self, shop: Shop) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        for product_name, amount in self.product_cart.items():
            if product_name in shop.products:
                cost_product = shop.products[product_name] * amount
                round_cost = (int(cost_product)
                              if cost_product == int(cost_product)
                              else cost_product)
                print(f"{amount} {product_name}s for "
                      f"{round_cost} dollars")
        total = sum(
            amount * shop.products[product_name]
            for product_name, amount in self.product_cart.items())

        print(f"Total cost is {round(total, 2)} dollars")
        print("See you again!\n")
