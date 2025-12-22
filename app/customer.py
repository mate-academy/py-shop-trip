import math
import datetime

from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        location: list,
        money: float,
        product_cart: dict,
        car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def get_distance(
        self,
        customer_location: list,
        shop_location: list
    ) -> float:
        return math.sqrt((customer_location[0] - shop_location[0]) ** 2
                         + (customer_location[1] - shop_location[1]) ** 2) * 2

    @staticmethod
    def calculate_fuel_cost(
        distance: float,
        fuel_price: float,
        fuel_consumption: float
    ) -> float:
        return distance / 100 * fuel_consumption * fuel_price

    def get_product_price(
        self,
        customer_products: dict,
        shop_products: dict
    ) -> float:
        total_price = 0
        for product in customer_products:
            if product in shop_products:
                total_price +=\
                    shop_products[product] * customer_products[product]
        return total_price

    def print_purchase_receipt(
        self,
        name: str,
        customer_products: dict,
        shop_products: dict
    ) -> float:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        total_price = 0
        for product in customer_products:
            if product in shop_products:
                price = shop_products[product] * customer_products[product]
                price = price if ".0" not in str(price) else int(price)
                total_price += price
                print(
                    f"{customer_products[product]} {product}s"
                    f" for {price} dollars"
                )
        print(f"Total cost is {total_price} dollars")
        print("See you again!" + "\n")

    def count_money(
        self, total_money: int,
        shop_price: int | float
    ) -> float | int:
        return total_money - shop_price
