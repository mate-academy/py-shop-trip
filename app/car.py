from __future__ import annotations
from dataclasses import dataclass
from app.location import Location


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def get_fuel(self, departure: Location, arrive: Location) -> float:
        distance = departure.calculate_distance(arrive)
        fuel = (distance * self.fuel_consumption) / 100
        return fuel
