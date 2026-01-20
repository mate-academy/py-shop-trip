from __future__ import annotations
from typing import List, Union

from app.customer.car import Car
from app.customer.product_cart import ProductCart


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: ProductCart,
        location: List[int],
        money: Union[int, float],
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def calculate_fuel_cost(
        self, destination: list, fuel_cost: float
    ) -> float:
        curr_x, curr_y = self.location
        dest_x, dest_y = destination

        distance = ((dest_x - curr_x) ** 2 + (dest_y - curr_y) ** 2) ** 0.5

        cost = (distance / 100) * self.car.fuel_consumption * fuel_cost * 2

        return round(cost, 2)

    @classmethod
    def from_dict(cls, customer: dict) -> Customer:
        return Customer(
            name=customer["name"],
            product_cart=ProductCart.from_fict(customer["product_cart"]),
            location=customer["location"],
            money=customer["money"],
            car=Car.from_dict(customer["car"]),
        )
