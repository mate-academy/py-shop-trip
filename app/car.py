from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_trip_cost(self, distance: float, fuel_price: float) -> float:
        return (distance / 100) * self.fuel_consumption * fuel_price
