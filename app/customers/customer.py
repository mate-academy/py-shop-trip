from app.customers.car import Car
from app.trips.point import Point


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int | float,
        car: dict,
    ) -> None:
        self.name = name
        self.cart = product_cart
        self.location = Point(*location)
        self.money = money
        self.car = Car(**car)
