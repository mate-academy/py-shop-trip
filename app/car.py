from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def road_fuel_consumption(self, dist_km: float):
        return self.fuel_consumption * dist_km / 100
