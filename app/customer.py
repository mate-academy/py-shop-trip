from typing import Any
from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def from_config(cls, data: dict[str, Any]) -> "Customer":
        car = Car.from_config(data["car"])
        return cls(
            name=data["name"],
            product_cart=data["product_cart"],
            location=data["location"],
            money=data["money"],
            car=car
        )
