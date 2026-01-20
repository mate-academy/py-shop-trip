from __future__ import annotations
from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def from_dict(cls, dictionary: dict) -> Customer:
        return cls(
            dictionary["name"],
            dictionary["product_cart"],
            dictionary["location"],
            dictionary["money"],
            Car.from_dict(dictionary["car"])
        )

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        total_distance = 2 * sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2)

        fuel_cost = ((total_distance / 100)
                     * self.car.fuel_consumption) * fuel_price
        total_cost = fuel_cost + shop.calculate_cart_cost(self.product_cart)

        return round(total_cost, 2)

    def rides_to(self, location: list[int], fuel_price: float) -> None:
        distance = sqrt(
            (self.location[0] - location[0]) ** 2
            + (self.location[1] - location[1]) ** 2
        )
        fuel_cost = (distance / 100) * self.car.fuel_consumption * fuel_price
        self.money -= fuel_cost
        self.location = location
