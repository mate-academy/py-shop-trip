from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        return self.fuel_consumption * distance * fuel_price / 100
