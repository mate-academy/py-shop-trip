from app.car import Car
import math


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int, int],
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = round(money, 2)
        self.car = car

    def calculate_distance(self,
                           destination: list[int, int]) -> float:

        return math.sqrt((destination[0] - self.location[0]) ** 2
                         + (destination[1] - self.location[1]) ** 2)
