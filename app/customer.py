import math
from dataclasses import dataclass
from typing import Dict
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int | float]
    location: list[int]
    money: int | float
    car: Car

    def return_home(
            self,
            initial_location: list[int],
            fuel_price: float
    ) -> None:
        distance_home = self.calculate_distance(initial_location)
        trip_cost = self.car.calculate_fuel_cost(distance_home, fuel_price)
        self.location = initial_location
        self.money -= trip_cost
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")

    def calculate_distance(self, destination: list[int]) -> float:
        distance1 = math.pow((self.location[0] - destination[0]), 2)
        distance2 = math.pow((self.location[1] - destination[1]), 2)
        dist = math.sqrt(distance1 + distance2)
        return round(dist * 2, 2)
