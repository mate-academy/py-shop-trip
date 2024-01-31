from math import sqrt
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def trip_cost(
            self,
            start_point: list[int],
            end_point: list[int],
            fuel_price: float
    ) -> float:
        distance = sqrt((start_point[0] - end_point[0]) ** 2
                        + (start_point[1] - end_point[1]) ** 2)
        fuel_needed = (distance / 100) * self.fuel_consumption
        total_cost = fuel_needed * fuel_price
        return total_cost
