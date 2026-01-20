import math
from datetime import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list[int],
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance_to_shop(self, shop_location: list) -> float:
        return math.dist(self.location, shop_location)

    def calculate_distance_price(self, shop: Shop, fuel_price: float) -> tuple:
        distance_to_shop = self.calculate_distance_to_shop(shop.location)
        fuel_cost = self.car.fuel_cost(distance_to_shop, fuel_price)
        products_cost = sum(
            self.product_cart[product] * price
            for product, price in shop.products.items()
            if product in self.product_cart
        )
        general_cost = round(2 * fuel_cost + products_cost, 2)
        return general_cost, round(products_cost, 2), round(fuel_cost, 2)

    def finalize_shopping(self, shop: Shop, fuel_price: float) -> None:
        general_cost, products_cost, fuel_cost = (
            self.calculate_distance_price(shop, fuel_price))
        current_time = (
            datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S"))

        if self.money < general_cost:
            print(f"{self.name} doesn't have enough"
                  f" money to make a purchase in {shop.name}")
            return

        self.money -= general_cost
        self.location = shop.location

        print(f"Date: {current_time}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_spent = 0
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                product_name = f"{product}s" if quantity > 1 else product
                price = round(quantity * shop.products[product], 2)
                formatted_price = str(price).rstrip("0").rstrip(".")
                print(f"{quantity} {product_name} "
                      f"for {formatted_price} dollars")
                total_spent += price

        formatted_total = str(round(total_spent, 2)).rstrip("0").rstrip(".")
        print(f"Total cost is {formatted_total} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")  # noqa: E231
