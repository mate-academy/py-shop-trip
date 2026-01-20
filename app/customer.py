from math import sqrt
from app.car import Car


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop_location: list) -> float:
        return sqrt((self.location[0] - shop_location[0]) ** 2 + (
            self.location[1] - shop_location[1]) ** 2)

    def update_location(self, new_location: list) -> None:
        self.location = new_location

    def has_enough_money(self, trip_cost: float) -> float:
        return self.money >= trip_cost

    def deduct_money(self, amount: float) -> None:
        self.money -= amount

    def add_money(self, amount: float) -> None:
        self.money += amount
