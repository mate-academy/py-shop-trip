import datetime
import math

from app.car import Car
from app.product import Products
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: Products,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to_shop(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 3)

    def have_enough_money(self, price: float) -> bool:
        return self.money >= price

    def groceries(self, other: Shop) -> float:
        return (self.product_cart.milk * other.products.milk
                + self.product_cart.bread * other.products.bread
                + self.product_cart.butter * other.products.butter)

    def print_check(self, other: Shop) -> None:
        date_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        milk = str(self.product_cart.milk * other.products.milk).rstrip(".0")
        bread = str(self.product_cart.bread
                    * other.products.bread).rstrip(".0")
        butter = str(self.product_cart.butter
                     * other.products.butter).rstrip(".0")
        print("")
        print(f"Date: {date_now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        print(f"{self.product_cart.milk} milks for {milk} dollars")
        print(f"{self.product_cart.bread} breads for {bread} dollars")
        print(f"{self.product_cart.butter} butters for {butter} dollars")
        print(f"Total cost is {self.groceries(other)} dollars")
        print("See you again!")
        print("")

    def all_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to_shop(shop)
        pay_trip = self.car.cost_for_trip(distance, fuel_price)
        return round(self.groceries(shop) + 2 * pay_trip, 2)

    def pay_for_groceries(self, check: float) -> None:
        self.money -= check
        print(f"{self.name} now has {self.money} dollars")
        print("")
