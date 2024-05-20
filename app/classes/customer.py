from __future__ import annotations

from app.classes.car import Car
from app.classes.from_dict import FromDict


class Customer(FromDict):
    def __init__(self,
                 name: str = "",
                 product_cart: dict = None,
                 location: list = None,
                 money: float = 0.0,
                 car: Car = Car()) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def from_dict(cls_dict: dict) -> Customer:
        new_customer = Customer()
        for key in cls_dict:
            if key == "car":
                setattr(new_customer, key, Car.from_dict(cls_dict[key]))
                continue
            setattr(new_customer, key, cls_dict[key])
        return new_customer
