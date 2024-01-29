from dataclasses import dataclass
from math import sqrt

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: Car

    def calculate_distance(self, destination: list[int]) -> float:
        num1 = (self.location[0] - destination[0]) ** 2
        num2 = (self.location[1] - destination[1]) ** 2
        distance = 2 * sqrt(num1 + num2)
        return round(distance, 2)

    def return_home(
            self,
            initial_location: list[int],
            fuel_price: float
    ) -> None:
        distance_to_home = self.calculate_distance(initial_location)
        trip_cost = self.car.calculate_fuel_cost(distance_to_home, fuel_price)
        self.location = initial_location
        self.money -= trip_cost

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")
