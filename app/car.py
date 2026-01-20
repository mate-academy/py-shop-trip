from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def litres_per_trip(self, distance: float) -> float:
        return (self.fuel_consumption * distance) / 100
