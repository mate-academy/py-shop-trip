from dataclasses import dataclass

from app.car.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int, int]
    money: float
    car: Car
