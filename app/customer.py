from typing import List
from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: int | float,
            car: dict,
    ) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car.get("brand"), car.get("fuel_consumption"))

    def money_start(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def ride_to_home(self) -> None:
        print(f"{self.name} rides home")

    def money_end(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")
