from copy import copy
import math

from app.car import Car


class Customer:
    def __init__(
            self, name: str, products_to_buy: dict,
            location: list, money: float, car: Car
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car
        self.home_location = copy(location)

    def distance_to(self, pn: list) -> float:
        return math.sqrt(
            (pn[0] - self.location[0]) ** 2 + (pn[1] - self.location[1]) ** 2
        )

    def trip_price_to(self, point2: list, fuel_price: float) -> float:
        return self.distance_to(point2) * self.car.price_per_1km(fuel_price)
