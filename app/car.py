from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(
            self,
            distance_km: float,
            fuel_price: float
    ) -> float:
        liters = distance_km * self.fuel_consumption / 100
        return liters * fuel_price
