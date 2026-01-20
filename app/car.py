from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_consumption_per_100_km(self, distance: float) -> float:
        return self.fuel_consumption / 100 * distance
