from __future__ import annotations
import math
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = location

    @classmethod
    def from_dict(cls, customer: dict) -> Customer:
        return cls(
            customer.get("name"),
            customer.get("product_cart"),
            customer.get("location"),
            customer.get("money"),
            Car.from_dict(customer.get("car"))
        )

    def calculate_trip_cost(
            self,
            destination: list,
            products: dict,
            fuel_price: float
    ) -> float:
        distance = round(
            math.sqrt(
                abs(self.location[0] - destination[0]) ** 2
                + abs(self.location[1] - destination[1]) ** 2
            ),
            4
        )
        fuel_cost = round(
            ((distance * 2) / 100) * self.car.fuel_consumption * fuel_price,
            2
        )

        product_cost = 0
        for product, quantity in self.product_cart.items():
            if product in products:
                product_cost += products[product] * quantity

        return product_cost + fuel_cost

    def __repr__(self) -> str:
        return f"{self.name}, {self.car}"
