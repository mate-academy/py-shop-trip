from math import dist

from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def move(self, new_location: list[int]) -> None:
        self.location = new_location

    def trip_cost(self, shop_location: list[int], fuel_price: float) -> float:
        distance = dist(self.location, shop_location)
        fuel_needed = distance * self.car.fuel_consumption / 100
        cost = fuel_needed * fuel_price

        return cost
