from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_total_consumption(self, distance: int | float) -> float:
        return distance * self.fuel_consumption / 100
