from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    def buy(self, cost: float) -> None:
        self.money -= cost
