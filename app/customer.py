from math import dist
import datetime

from app.car import Car, create_car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.car = car
        self.money = money
        self.location = location
        self.product_cart = product_cart
        self.name = name
        self.spent_money = 0

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel_cost = (dist(self.location, shop.location)
                     * self.car.fuel_consumption * fuel_price) * 2
        products_cost = 0
        for name, count in self.product_cart.items():
            products_cost += shop.products[name] * count
        return round(products_cost + fuel_cost, 2)

    def remaining_money(self) -> None:
        print(f"\n{self.name} rides home\n{self.name} "
              f"now has {self.money - self.spent_money} dollars\n")

    def arrived_to_shop(self, shop: Shop, spent_money: float) -> None:
        self.spent_money = spent_money
        self.location = shop.location

    def create_receipt(self, shop: Shop) -> None:
        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought: ")
        bill = 0
        for product, count in self.product_cart.items():
            bill += shop.products[product] * count
            print(f"{count} {product}s "
                  f"for {shop.products[product] * count} dollars")
        print(f"Total cost is {bill} dollars\nSee you again!")


def create_customer(customer: dict) -> Customer:
    return Customer(name=customer["name"],
                    product_cart=customer["product_cart"],
                    location=customer["location"],
                    money=customer["money"],
                    car=create_car(customer["car"]))
