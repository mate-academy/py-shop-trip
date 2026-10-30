from math import sqrt

from car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[float],
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(
        self,
        destination: list[float],
    ) -> float:
        return sqrt(
            (self.location[0] - destination[0]) ** 2
            + (self.location[1] - destination[1]) ** 2
        )
