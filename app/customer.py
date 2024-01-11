from typing import List
from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int | float
    car: Car

    def money_start(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def ride_to_home(self) -> None:
        print(f"{self.name} rides home")

    def money_end(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")
