import dataclasses

from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    products_to_buy: dict
    location: list[int]
    money: int
    car: Car
