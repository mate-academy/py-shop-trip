from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def amount_of_fuel(self, distance: float) -> float:
        return 2 * distance * self.fuel_consumption / 100
