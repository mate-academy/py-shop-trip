from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_expense(self, distance: float) -> float:
        return self.fuel_consumption * distance / 100
