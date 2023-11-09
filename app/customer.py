import datetime
import math

from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            money: int,
            product_cart: dict,
            location: list,
            car_fuel_consumption: float
    ):
        self.name = name
        self.money = money
        self.product_cart = product_cart
        self.location = location
        self.car_fuel_consumption = car_fuel_consumption

    def buy_products(self, shop: Shop):
        print("You have bought: ")
        total = 0

        for product in self.product_cart:
            price = self.product_cart[product] * shop.products[product]
            print(
                f"{self.product_cart[product]} {product}s for {price} dollars"
            )
            total += price

        return total

    def count_expenses(self, shop: Shop, fuel_consumption: float):
        total_money = 0

        for product in self.product_cart:
            total_money += self.product_cart[product] * shop.products[product]

        distance_to_shop = math.dist(shop.location, self.location) * 2
        used_fuel = distance_to_shop * fuel_consumption
        money_spend_on_fuel = round(
            self.car_fuel_consumption / 100 * used_fuel,
            2
        )
        total_money += money_spend_on_fuel

        return total_money

    def going_to_shop(self, shop: Shop, money: float):
        print(f"{self.name} rides to {shop.name}\n")
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")

        total = self.buy_products(shop)

        print(f"Total cost is {total} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - money} dollars\n")
