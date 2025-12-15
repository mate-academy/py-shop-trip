from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_trip_cost(self, distance: float, fuel_price: float) -> float:
        fuel_needed = (distance / 100) * self.fuel_consumption
        return round(fuel_needed * fuel_price, 2)
