from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_for_one_km(self) -> float:
        return self.fuel_consumption / 100
