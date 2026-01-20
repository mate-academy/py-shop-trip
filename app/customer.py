from app.car import Car
import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car
