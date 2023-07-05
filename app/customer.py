import dataclasses

from app.car import Car


@dataclasses.dataclass
class Customers:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car
