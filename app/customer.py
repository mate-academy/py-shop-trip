from app.car import Car
from app.shop import Shop
import math


def distance(a_coord: list[float], b_coord: list[float]) -> float:
    return math.sqrt((a_coord[0] - b_coord[0])
                     ** 2 + (a_coord[1] - b_coord[1]) ** 2)


class Customer:
    def __init__(self,
                 name: str,
                 cart: dict,
                 location: list,
                 money: int | float,
                 car: Car) -> None:
        self.name = name
        self.cart = cart
        self.location = location
        self.money = money
        self.car = car
        self.home = location[:]

    def can_afford(self, shop: Shop, fuel_price: float) -> tuple[bool, float]:
        dist = distance(self.location, shop.location)
        fuel_needed = (dist * 2) * self.car.fuel_consumption / 100
        fuel_cost = fuel_needed * fuel_price
        product_cost = shop.calculate_cart_cost(self.cart)
        total = round(product_cost + fuel_cost, 2)
        return total <= self.money, total

    def go_to(self, location: list) -> None:
        self.location = location[:]

    def go_home(self) -> None:
        self.location = self.home[:]
